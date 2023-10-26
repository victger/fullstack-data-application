from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from typing import Optional
import datetime

class Post(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    title: str
    description: Optional[str]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]