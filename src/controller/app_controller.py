import os
from model.reddit_scraper import RedditScraper
from view.card_generator import CardGenerator
from view.style_manager import StyleManager
from model.category_config import CONTENT_CATEGORIES

class AppController:
    def __init__(self, config_path=None):
        self.scraper = RedditScraper(config_path)
        self.style_manager = StyleManager(self.scraper.config)
        self.card_generator = CardGenerator(self.style_manager)
        self.output_dir = self.scraper.config.get('output_dir', 'output')
        os.makedirs(self.output_dir, exist_ok=True)

    def select_and_run(self):
        import re
        import time
        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        def clean_title(title):
            cleaned = re.sub(r'[\\/:*?"<>|]', '', title)
            cleaned = cleaned.strip().replace('\n', ' ')
            return cleaned[:60] if len(cleaned) > 60 else cleaned
        while True:
            clear()
            print("\n" + "=" * 60)
            print("  GÉNÉRATEUR DE CONTENU REDDIT  ".center(60))
            print("=" * 60 + "\n")
            # Demander le nombre de sujets à traiter
            try:
                post_count = int(input("Combien de sujets Reddit voulez-vous traiter ? [1-20] : "))
                if not (1 <= post_count <= 20):
                    print("Veuillez entrer un nombre entre 1 et 20.")
                    time.sleep(1.5)
                    continue
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
                time.sleep(1.5)
                continue
            # Afficher les catégories
            print("Catégories de contenu disponibles :\n")
            for key, cat in CONTENT_CATEGORIES.items():
                print(f"{key}. {cat['name']} - {cat['description']}")
            print("\n0. Quitter\n")
            cat_key = input(f"Choisissez une catégorie (0-{len(CONTENT_CATEGORIES)}): ").strip()
            if cat_key == "0":
                clear()
                print("Merci d'avoir utilisé le Générateur de Contenu Reddit !")
                break
            if cat_key not in CONTENT_CATEGORIES:
                print("Catégorie invalide. Veuillez réessayer.")
                time.sleep(1.5)
                continue
            clear()
            cat = CONTENT_CATEGORIES[cat_key]
            print(f"\n{cat['name']} - {cat['description']}\n")
            print("Options disponibles :\n")
            for idx, opt in enumerate(cat['options']):
                print(f"{idx+1}. r/{opt['subreddit']} - Tri: {opt['sorting']} - Période: {opt['timeframe']}")
            print("\n0. Retour\n")
            try:
                opt_choice = input(f"Choisissez une option (0-{len(cat['options'])}): ")
                if opt_choice == "0":
                    continue
                opt_idx = int(opt_choice) - 1
                if not (0 <= opt_idx < len(cat['options'])):
                    print("Option invalide. Veuillez réessayer.")
                    time.sleep(1.5)
                    continue
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
                time.sleep(1.5)
                continue
            opt = cat['options'][opt_idx]
            subreddit = opt['subreddit']
            print(f"\nTraitement de {post_count} posts sur r/{subreddit} ...\n")
            posts = self.scraper.fetch_posts_with_params(
                subreddit,
                post_count=post_count,
                sorting=opt['sorting'],
                timeframe=opt.get('timeframe'),
                comment_count=opt.get('comment_count', 10),
                allow_nsfw=opt.get('allow_nsfw', False),
                min_comment_length=30
            )
            for post in posts:
                folder_name = clean_title(post.title)
                post_dir = os.path.join(self.output_dir, folder_name)
                os.makedirs(post_dir, exist_ok=True)
                title_path = os.path.join(post_dir, 'title.png')
                self.card_generator.create_title_card(post.title, getattr(post, 'subreddit', opt['subreddit']), post.author, title_path, show_likes=True, show_pseudo=True)
                for idx, comment in enumerate(post.comments[:10]):
                    comment_path = os.path.join(post_dir, f'comment_{idx+1}.png')
                    self.card_generator.create_comment_card(comment.body, comment.author, comment.score, comment_path)
                # Création du fichier contextuel Markdown
                post_url = f'https://www.reddit.com/r/{post.subreddit}/comments/{post.id}/'
                # Recherche d'URL vidéo dans le titre ou les 10 premiers commentaires
                video_urls = []
                url_pattern = r'(https?://[\w\.-]+\.(?:mp4|mov|webm|mkv|avi|youtube\.com|youtu\.be|vimeo\.com|twitter\.com|tiktok\.com)[^\s]*)'
                if re.search(url_pattern, post.title, re.IGNORECASE):
                    video_urls.extend(re.findall(url_pattern, post.title, re.IGNORECASE))
                for c in post.comments[:10]:
                    video_urls.extend(re.findall(url_pattern, c.body, re.IGNORECASE))
                video_urls = list(set(video_urls))
                video_urls_str = '\n'.join(video_urls) if video_urls else 'Aucune vidéo'
                # Description contextuelle
                description = getattr(post, 'description', None) or post.title
                # Section commentaires
                commentaires_md = ''
                for i, c in enumerate(post.comments[:10]):
                    commentaires_md += f"- {i+1}. {c.body.strip().replace(chr(10), ' ')}\n"
                # Contexte viral (simple résumé basé sur le titre et le nombre de commentaires)
                contexte_md = f"Ce post a généré de nombreux commentaires et réactions sur le sujet : '{post.title}'. Il semble avoir un effet viral ou susciter un débat important dans la communauté r/{post.subreddit}."
                # Bloc story/contexte narratif (jamais d'image ni url markdown)
                story_block = ''
                story_img_path = os.path.join(post_dir, 'story.png')
                # Si selftext existe, affiche le texte brut (jamais d’image ni d’URL)
                if hasattr(post, 'selftext') and post.selftext and post.selftext.strip():
                    self.card_generator.create_comment_card(post.selftext.strip(), post.author, output_path=story_img_path, likes=None, pseudo='', show_likes=False)
                    story_block = f"\n\n**Story complète ou contexte narratif :**\n\n{post.selftext.strip()}\n"
                # Si submission.url existe (image ou vidéo), ajoute l’URL brute dans le bloc markdown (même si selftext existe)
                if hasattr(post, 'url') and post.url:
                    story_block += f"\n\n**Lien du contenu (image ou vidéo) :**\n{post.url}\n"
                # Si rien, fallback sur le titre
                if not story_block.strip():
                    story_block = f"\n\n**Story complète ou contexte narratif :**\n\n{post.title}\n"
                # Construction du markdown
                md = f"""---
**Titre** : {post.title}
**Subreddit** : r/{post.subreddit}
**Tri** : {opt['sorting']}
**Période** : {opt.get('timeframe','')}
**URL du post** : {post_url}
**URL vidéo (si présente)** : {video_urls_str}
**Description** : {description}
**Commentaires** :
{commentaires_md}
**Contexte** : {contexte_md}
{story_block}
"""
                context_path = os.path.join(post_dir, f"context_{post.id}.md")
                os.makedirs(os.path.dirname(context_path), exist_ok=True)
                with open(context_path, "w", encoding="utf-8") as f:
                    f.write(md)

            print(f"\nGénération terminée ! Images sauvegardées dans {self.output_dir}\n")
            input("Appuyez sur Entrée pour continuer...")
