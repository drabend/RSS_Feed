from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas import FeedCreate, FeedOut

from services.feed_services import create_feed as create_feed_service
from services.feed_services import get_all_feeds as get_all_feeds_service
from services.feed_services import get_feed as get_feed_service
from services.feed_services import delete_feed as delete_feed_service
from services.feed_parser import parse_feed as parse_feed_service
router = APIRouter()

# Get all feeds
@router.get("/feeds/", description="Returns all available feeds")
def get_feeds(db: Session = Depends(get_db)):
    feeds = get_all_feeds_service(db)
    return feeds
# Add a new feed
@router.post("/feeds/", description="Add a new feed", response_model=FeedOut)
def create_feed(payload: FeedCreate, db: Session = Depends(get_db)):
    return create_feed_service(db, link=str(payload.link))


# Delete a feed
@router.delete("/feeds/{feed_id}/", description="Delete a feed by id")
def delete_feed(feed_id: int, db: Session = Depends(get_db)):
    delete_feed_service(db, id=feed_id)


# Get a feed by id
@router.get("/feeds/{feed_id}/", description="Get a feed by id", response_model=FeedOut)
def get_feed(feed_id: int, db: Session = Depends(get_db)):
    return get_feed_service(db, id=feed_id)

# parse a feeds content by id
@router.get("/feeds/{feed_id}/parse/", description="Parse a feeds content by id")
def parse_feed(feed_id: int, db: Session = Depends(get_db)):
    return parse_feed_service(db, id=feed_id)