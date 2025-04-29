# Catégories et options inspirées du content_selector.py d'origine
CONTENT_CATEGORIES = {
    "1": {
        "name": "🌍 Actus & Réactions",
        "description": "Sujets d'actualité qui font réagir, polémiques et débats mondiaux.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "worldnews", "sorting": "controversial", "timeframe": "week", "post_count": 20},
            {"subreddit": "news", "sorting": "controversial", "timeframe": "week", "post_count": 20},
            {"subreddit": "politics", "sorting": "controversial", "timeframe": "month", "post_count": 15},
            {"subreddit": "geopolitics", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "2": {
        "name": "🤖 IA & Tech qui Divisent",
        "description": "Avancées, débats et questions controversées sur l'IA et la tech.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "ArtificialIntelligence", "sorting": "controversial", "timeframe": "week", "post_count": 20},
            {"subreddit": "MachineLearning", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "GPT3", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "3": {
        "name": "💻 Dev & Geek Clash",
        "description": "Débats, clashs et questions qui font réagir les devs et geeks.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "webdev", "sorting": "controversial", "timeframe": "month", "post_count": 15},
            {"subreddit": "programming", "sorting": "controversial", "timeframe": "month", "post_count": 15},
            {"subreddit": "learnprogramming", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "4": {
        "name": "💄 Beauté & Jugements",
        "description": "Tendances, polémiques et débats du monde de la beauté.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "MakeupAddiction", "sorting": "controversial", "timeframe": "month", "post_count": 15},
            {"subreddit": "SkincareAddiction", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "Sephora", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "5": {
        "name": "🤣 Humour qui Divise",
        "description": "Blagues, histoires et posts qui polarisent ou font débat.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "jokes", "sorting": "controversial", "timeframe": "month", "post_count": 15},
            {"subreddit": "funny", "sorting": "controversial", "timeframe": "week", "post_count": 15},
            {"subreddit": "tifu", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "maliciouscompliance", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "6": {
        "name": "🔥 Débats & Polémiques",
        "description": "Les sujets qui divisent, choquent ou créent un raz-de-marée de commentaires.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "unpopularopinion", "sorting": "controversial", "timeframe": "week", "post_count": 20},
            {"subreddit": "changemyview", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "TooAfraidToAsk", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "confessions", "sorting": "top", "timeframe": "week", "post_count": 15}
        ]
    },
    "7": {
        "name": "🚀 Buzz & Comment Wars",
        "description": "Histoires, avis tranchés et posts qui déclenchent des guerres de commentaires.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "amitheasshole", "sorting": "controversial", "timeframe": "week", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "BestofRedditorUpdates", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "relationships", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "relationship_advice", "sorting": "top", "timeframe": "month", "post_count": 15}
        ]
    },
    "8": {
        "name": "💬 Questions Ultra Commentées",
        "description": "Les posts qui génèrent des milliers de réponses et débats ouverts.",
        "frequency": "daily",
        "options": [
            {"subreddit": "AskReddit", "sorting": "top", "timeframe": "day", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "AskReddit", "sorting": "top", "timeframe": "week", "post_count": 20, "comment_sort": "most_comments"},
            {"subreddit": "AskMen", "sorting": "top", "timeframe": "week", "post_count": 15, "comment_sort": "most_comments"},
            {"subreddit": "AskWomen", "sorting": "top", "timeframe": "week", "post_count": 15, "comment_sort": "most_comments"}
        ]
    },
    "9": {
        "name": "Football ⚽",
        "description": "Dernières tendances et réactions autour du football mondial.",
        "frequency": "daily",
        "options": [
            {"subreddit": "soccer", "sorting": "hot", "timeframe": "day", "post_count": 15},
            {"subreddit": "football", "sorting": "top", "timeframe": "week", "post_count": 10}
        ]
    },
    "10": {
        "name": "NBA 🏀",
        "description": "Tout ce qui buzz autour de la NBA et du basketball.",
        "frequency": "daily",
        "options": [
            {"subreddit": "nba", "sorting": "hot", "timeframe": "day", "post_count": 12}
        ]
    },
    "11": {
        "name": "DevOps 🚀",
        "description": "Conseils, astuces et anecdotes DevOps pour rester à jour et se divertir.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "devops", "sorting": "top", "timeframe": "month", "post_count": 10}
        ]
    },
    "12": {
        "name": "Intelligence Artificielle 🤖",
        "description": "Découvertes, applications et discussions sur l'IA.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "ArtificialIntelligence", "sorting": "hot", "timeframe": "week", "post_count": 12}
        ]
    },
    "13": {
        "name": "Tendances Générales 🌍",
        "description": "Les contenus populaires qui font réagir tout le monde.",
        "frequency": "daily",
        "options": [
            {"subreddit": "AskReddit", "sorting": "top", "timeframe": "day", "post_count": 15}
        ]
    }
}
