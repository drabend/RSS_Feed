from pydantic import BaseModel, AnyUrl

class FeedCreate(BaseModel):
    link: AnyUrl

class FeedOut(BaseModel):
    id: int
    link: AnyUrl

    class Config:
        from_attributes = True