from sqlalchemy.orm import Session
from services.feed_services import get_feed
from feedparser import parse

def parse_feed(db: Session, id: int):
    feed = get_feed(db, id)
    link = feed.link
    parsed_feed = parse(link)

    if parsed_feed.status != 200:
        return {"error": "Failed to parse feed"}

    return parsed_feed

