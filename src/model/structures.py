# Structures de données pour Post et Comment
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Comment:
    author: str
    body: str
    score: int
    id: str

@dataclass
class Post:
    title: str
    author: str
    score: int
    id: str
    subreddit: str
    comments: List[Comment]
