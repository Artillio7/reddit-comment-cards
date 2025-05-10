import praw
from typing import List
from model.structures import Post, Comment
import yaml
import os
from dotenv import load_dotenv
load_dotenv()

class RedditScraper:
    def __init__(self, config_path: str = None):
        # Configuration par défaut
        self.config = {
            'output_dir': 'output',
            'max_comments': 10,
            'min_comment_length': 30
        }
        
        # Préparer l'API Reddit
        self.reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT', 'reddit-comment-cards'),
            password=os.getenv('REDDIT_PASSWORD', '')
        )

    def fetch_posts(self) -> List[Post]:
        subreddit = self.config.get('subreddit', 'AskReddit')
        post_count = self.config.get('post_count', 1)
        comment_count = self.config.get('comment_count', 10)
        sort = self.config.get('sort', 'top')

        return self.fetch_posts_with_params(subreddit, post_count, sort, None, comment_count)

    def fetch_posts_with_params(self, subreddit, post_count=1, sorting='top', timeframe=None, comment_count=10, allow_nsfw=False, min_comment_length=30):
        sub = self.reddit.subreddit(subreddit)
        # Récupérer plus de posts pour filtrer ensuite
        fetch_limit = min(post_count * 4, 100)
        if sorting == 'hot':
            posts = sub.hot(limit=fetch_limit)
        elif sorting == 'new':
            posts = sub.new(limit=fetch_limit)
        elif sorting == 'rising':
            posts = sub.rising(limit=fetch_limit)
        elif sorting == 'controversial':
            posts = sub.controversial(time_filter=timeframe or 'week', limit=fetch_limit)
        else:
            posts = sub.top(time_filter=timeframe or 'week', limit=fetch_limit)

        result = []
        for submission in posts:
            # Filtrage NSFW
            if submission.over_18 and not allow_nsfw:
                continue
            # Vérifier qu'il y a un titre
            if not submission.title:
                continue
            # Préparer les commentaires
            submission.comment_sort = 'best'
            try:
                submission.comments.replace_more(limit=0)
            except Exception:
                continue
            comments = [c for c in submission.comments if not getattr(c, 'stickied', False) and hasattr(c, 'body') and c.body and len(c.body) >= min_comment_length]
            # Trier les commentaires par score décroissant
            comments = sorted(comments, key=lambda c: getattr(c, 'score', 0), reverse=True)
            # Prendre les N meilleurs commentaires pertinents
            top_comments = comments[:comment_count]
            if len(top_comments) < 3:
                continue  # On veut au moins 3 bons commentaires par post
            comment_objs = [Comment(author=getattr(c.author, 'name', '[deleted]'), body=c.body, score=c.score, id=c.id) for c in top_comments]
            result.append(Post(
                title=submission.title,
                author=getattr(submission.author, 'name', '[deleted]'),
                score=submission.score,
                id=submission.id,
                subreddit=submission.subreddit.display_name,
                comments=comment_objs,
                selftext=getattr(submission, 'selftext', ''),
                url=getattr(submission, 'url', '')
            ))
            if len(result) >= post_count:
                break
        return result
