# Catégories et options inspirées du content_selector.py d'origine
CONTENT_CATEGORIES = {
    "1": {
        "name": "🌍 Actus & Réactions",
        "description": "Sujets d'actualité qui font réagir, polémiques et débats mondiaux.",
        "frequency": "daily",
        "options": [
            {"subreddit": "worldnews", "sorting": "controversial", "timeframe": "day", "post_count": 10, "comment_threshold": 100},
            {"subreddit": "news", "sorting": "top", "timeframe": "day", "post_count": 10, "upvote_ratio": 0.8},
            {"subreddit": "politics", "sorting": "rising", "timeframe": "week", "post_count": 10, "exclude_keywords": ["meme", "fluff"]},
            {"subreddit": "geopolitics", "sorting": "new", "timeframe": "week", "post_count": 5}
        ]
    },
    "2": {
        "name": "🤖 IA & Tech qui Divisent",
        "description": "Discussions sur l'intelligence artificielle et les technologies émergentes.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "artificial", "sorting": "controversial", "timeframe": "week", "post_count": 10, "comment_threshold": 80},
            {"subreddit": "MachineLearning", "sorting": "rising", "timeframe": "month", "post_count": 8, "upvote_ratio": 0.7},
            {"subreddit": "GPT3", "sorting": "top", "timeframe": "month", "post_count": 8},
            {"subreddit": "OpenAI", "sorting": "new", "timeframe": "week", "post_count": 5}
        ]
    },
    "3": {
        "name": "Développement Web",
        "description": "Programmation et développement fullstack.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "webdev", "sorting": "rising", "timeframe": "week", "post_count": 8},
            {"subreddit": "programming", "sorting": "top", "timeframe": "week", "post_count": 8, "exclude_keywords": ["beginner"]},
            {"subreddit": "learnprogramming", "sorting": "new", "timeframe": "week", "post_count": 8}
        ]
    },
    "4": {
        "name": "💄 Beauté & Jugements",
        "description": "Tendances, polémiques et débats du monde de la beauté.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "MakeupAddiction", "sorting": "top", "timeframe": "month", "post_count": 8},
            {"subreddit": "SkincareAddiction", "sorting": "rising", "timeframe": "month", "post_count": 8},
            {"subreddit": "Sephora", "sorting": "new", "timeframe": "month", "post_count": 8}
        ]
    },
    "5": {
        "name": "🤣 Humour qui Divise",
        "description": "Blagues, histoires et posts qui polarisent ou font débat.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "jokes", "sorting": "top", "timeframe": "month", "post_count": 8, "upvote_ratio": 0.7},
            {"subreddit": "funny", "sorting": "rising", "timeframe": "week", "post_count": 8},
            {"subreddit": "tifu", "sorting": "new", "timeframe": "month", "post_count": 8},
            {"subreddit": "maliciouscompliance", "sorting": "controversial", "timeframe": "month", "post_count": 8}
        ]
    },
    "6": {
        "name": "Contenu Viral à Fort Engagement",
        "description": "Posts narratifs, émotionnels et polarisants avec engagement maximal.",
        "frequency": "daily",
        "options": [
            {"subreddit": "AskReddit", "sorting": "rising", "timeframe": "day", "post_count": 12, "comment_sort": "best"},
            {"subreddit": "amitheasshole", "sorting": "controversial", "timeframe": "week", "post_count": 10, "comment_sort": "top", "comment_threshold": 200},
            {"subreddit": "tifu", "sorting": "top", "timeframe": "week", "post_count": 8, "comment_sort": "q&a"},
            {"subreddit": "relationships", "sorting": "new", "timeframe": "week", "post_count": 8, "comment_sort": "controversial"}
        ]
    },
    "7": {
        "name": "🚀 Buzz & Comment Wars",
        "description": "Histoires, avis tranchés et posts qui déclenchent des guerres de commentaires.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "amitheasshole", "sorting": "rising", "timeframe": "week", "post_count": 10, "comment_sort": "most_comments"},
            {"subreddit": "BestofRedditorUpdates", "sorting": "top", "timeframe": "month", "post_count": 8},
            {"subreddit": "relationships", "sorting": "controversial", "timeframe": "month", "post_count": 8},
            {"subreddit": "relationship_advice", "sorting": "new", "timeframe": "month", "post_count": 8}
        ]
    },
    "8": {
        "name": "💬 Questions Ultra Commentées",
        "description": "Questions qui suscitent le plus de récits et d'avis personnels.",
        "frequency": "daily",
        "options": [
            {"subreddit": "AskReddit", "sorting": "top", "timeframe": "day", "post_count": 15, "comment_sort": "best"},
            {"subreddit": "AskReddit", "sorting": "controversial", "timeframe": "week", "post_count": 10, "comment_sort": "controversial"},
            {"subreddit": "tifu", "sorting": "new", "timeframe": "week", "post_count": 8, "comment_sort": "q&a"},
            {"subreddit": "amitheasshole", "sorting": "top", "timeframe": "week", "post_count": 8, "comment_sort": "top"}
        ]
    },
    "9": {
        "name": "Football ⚽",
        "description": "Dernières tendances et réactions autour du football mondial.",
        "frequency": "daily",
        "options": [
            {"subreddit": "soccer", "sorting": "rising", "timeframe": "day", "post_count": 8},
            {"subreddit": "football", "sorting": "top", "timeframe": "week", "post_count": 5}
        ]
    },
    "10": {
        "name": "NBA 🏀",
        "description": "Tout ce qui buzz autour de la NBA et du basketball.",
        "frequency": "daily",
        "options": [
            {"subreddit": "nba", "sorting": "new", "timeframe": "day", "post_count": 6}
        ]
    },
    "11": {
        "name": "DevOps 🚀",
        "description": "Conseils, astuces et anecdotes DevOps pour rester à jour et se divertir.",
        "frequency": "monthly",
        "options": [
            {"subreddit": "devops", "sorting": "rising", "timeframe": "month", "post_count": 5}
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
    },
    "14": {
        "name": "Art et Design 🎨",
        "description": "Créations artistiques, techniques et discussions sur l'art visuel.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "Art", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "ArtFundamentals", "sorting": "top", "timeframe": "month", "post_count": 10},
            {"subreddit": "drawing", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "streetwear", "sorting": "top", "timeframe": "week", "post_count": 10}
        ]
    },
    "15": {
        "name": "Cinéma et Séries 🎬",
        "description": "Discussions, critiques et recommandations sur le monde audiovisuel.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "movies", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "MovieSuggestions", "sorting": "top", "timeframe": "month", "post_count": 15},
            {"subreddit": "truefilm", "sorting": "top", "timeframe": "month", "post_count": 10},
            {"subreddit": "television", "sorting": "hot", "timeframe": "week", "post_count": 15}
        ]
    },
    "16": {
        "name": "Cuisine et Gastronomie 🍲",
        "description": "Recettes, techniques culinaires et conseils pour tous niveaux.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "Cooking", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "EatCheapAndHealthy", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "MealPrepSunday", "sorting": "top", "timeframe": "week", "post_count": 10},
            {"subreddit": "AskCulinary", "sorting": "hot", "timeframe": "week", "post_count": 10}
        ]
    },
    "17": {
        "name": "Littérature et Lectures 📚",
        "description": "Suggestions de livres, discussions littéraires et critiques.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "books", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "suggestmeabook", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "52book", "sorting": "top", "timeframe": "month", "post_count": 10},
            {"subreddit": "TrueLit", "sorting": "top", "timeframe": "month", "post_count": 10}
        ]
    },
    "18": {
        "name": "Mode et Tendances 👗",
        "description": "Dernières tendances, conseils mode et discussions sur l'industrie.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "malefashionadvice", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "femalefashionadvice", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "streetwear", "sorting": "top", "timeframe": "week", "post_count": 15},
            {"subreddit": "Sneakers", "sorting": "top", "timeframe": "week", "post_count": 10}
        ]
    },
    "19": {
        "name": "Philo & Opinions 💭",
        "description": "Débats d'idées, opinions tranchées et réflexions philosophiques.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "changemyview", "sorting": "top", "timeframe": "week", "post_count": 10, "comment_sort": "best"},
            {"subreddit": "TrueOffMyChest", "sorting": "controversial", "timeframe": "week", "post_count": 8, "comment_sort": "controversial"},
            {"subreddit": "unpopularopinion", "sorting": "rising", "timeframe": "week", "post_count": 8, "comment_sort": "top"}
        ]
    },
    "20": {
        "name": "Insolite & WTF 🤯",
        "description": "Conseils légaux, questions insolites, confessions et situations inattendues.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "legaladvice", "sorting": "top", "timeframe": "week", "post_count": 8, "comment_sort": "best"},
            {"subreddit": "NoStupidQuestions", "sorting": "rising", "timeframe": "week", "post_count": 8, "comment_sort": "q&a"},
            {"subreddit": "confession", "sorting": "controversial", "timeframe": "week", "post_count": 8, "comment_sort": "controversial"}
        ]
    },
    "21": {
        "name": "Récits de vie & Authenticité 📝",
        "description": "Histoires vraies, conseils de vie, authenticité et revanche du quotidien.",
        "frequency": "weekly",
        "options": [
            {"subreddit": "LifeProTips", "sorting": "top", "timeframe": "week", "post_count": 8, "comment_sort": "best"},
            {"subreddit": "PettyRevenge", "sorting": "controversial", "timeframe": "week", "post_count": 8, "comment_sort": "top"},
            {"subreddit": "OffMyChest", "sorting": "new", "timeframe": "week", "post_count": 8, "comment_sort": "controversial"}
        ]
    }
}
