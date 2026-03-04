from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Feed

# returns all feeds
def get_all_feeds(db: Session):
    return db.query(Feed).all()

# creates a new feed
def create_feed(db: Session, link: str):
    feed = db.query(Feed).filter(Feed.link == link).first()

    # if feed exists with the same link
    if feed:
        raise HTTPException(status_code=409, detail="exists")

    feed = Feed(link=link)
    db.add(feed)
    db.commit()
    db.refresh(feed)
    return feed

# returns feed by id
def get_feed(db: Session, id: int):
    feed = db.query(Feed).filter(Feed.id == id).first()
    if not feed:
        raise HTTPException(status_code=404, detail="not found")

    return feed