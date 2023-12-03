from typing import List
from db.database import data


def define_themes(query: str) -> List:
    matched_themes = []
    query = query.lower()
    words = set(query.split())
    for theme, text in data.items():
        if any(all(word.lower() in words for word in phrase.split()) for phrase in text):
            matched_themes.append(theme)
    return matched_themes
