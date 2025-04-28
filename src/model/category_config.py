# Catégories et options inspirées du content_selector.py d'origine
CONTENT_CATEGORIES = {
    "1": {
        "name": "Actualités Mondiales",
        "description": "Dernières actualités et événements mondiaux",
        "options": [
            {"subreddit": "worldnews", "sorting": "hot", "timeframe": "day", "post_count": 20},
            {"subreddit": "news", "sorting": "hot", "timeframe": "day", "post_count": 20},
            {"subreddit": "politics", "sorting": "hot", "timeframe": "day", "post_count": 15},
            {"subreddit": "geopolitics", "sorting": "top", "timeframe": "week", "post_count": 15}
        ]
    },
    "2": {
        "name": "Intelligence Artificielle",
        "description": "Discussions et avancées en IA",
        "options": [
            {"subreddit": "artificial", "sorting": "hot", "timeframe": "week", "post_count": 20},
            {"subreddit": "MachineLearning", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "GPT3", "sorting": "hot", "timeframe": "week", "post_count": 15}
        ]
    },
    "3": {
        "name": "Développement Web",
        "description": "Programmation et développement fullstack",
        "options": [
            {"subreddit": "webdev", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "programming", "sorting": "hot", "timeframe": "week", "post_count": 15},
            {"subreddit": "learnprogramming", "sorting": "top", "timeframe": "week", "post_count": 15}
        ]
    },
    "4": {
        "name": "Beauté et Cosmétiques",
        "description": "Produits de beauté, revues et conseils",
        "options": [
            {"subreddit": "MakeupAddiction", "sorting": "hot", "timeframe": "week", "post_count": 15},
            {"subreddit": "SkincareAddiction", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "Sephora", "sorting": "hot", "timeframe": "month", "post_count": 15}
        ]
    },
    "5": {
        "name": "Humour et Divertissement",
        "description": "Blagues, histoires drôles et contenus divertissants",
        "options": [
            {"subreddit": "jokes", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "funny", "sorting": "hot", "timeframe": "day", "post_count": 15},
            {"subreddit": "tifu", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "maliciouscompliance", "sorting": "top", "timeframe": "week", "post_count": 15}
        ]
    },
    "6": {
        "name": "Contenu Viral à Fort Engagement",
        "description": "Posts avec le plus fort taux d'engagement",
        "options": [
            {"subreddit": "askreddit", "sorting": "hot", "timeframe": "day", "post_count": 20},
            {"subreddit": "amitheasshole", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "unpopularopinion", "sorting": "controversial", "timeframe": "week", "post_count": 15},
            {"subreddit": "relationship_advice", "sorting": "hot", "timeframe": "day", "post_count": 15}
        ]
    },
    "7": {
        "name": "Conseils et Explications",
        "description": "Conseils pratiques et explications de concepts",
        "options": [
            {"subreddit": "lifeprotips", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "explainlikeimfive", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "YouShouldKnow", "sorting": "top", "timeframe": "week", "post_count": 15}
        ]
    },
    "8": {
        "name": "Questions les Plus Populaires",
        "description": "Questions qui ont généré le plus de réponses",
        "options": [
            {"subreddit": "askreddit", "sorting": "top", "timeframe": "day", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "askreddit", "sorting": "top", "timeframe": "week", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "askreddit", "sorting": "top", "timeframe": "month", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "nostupidquestions", "sorting": "top", "timeframe": "week", "post_count": 15, "comment_sort": "most_comments"},
            {"subreddit": "AskMen", "sorting": "top", "timeframe": "week", "post_count": 15, "comment_sort": "most_comments"},
            {"subreddit": "AskWomen", "sorting": "top", "timeframe": "week", "post_count": 15, "comment_sort": "most_comments"}
        ]
    }
}
