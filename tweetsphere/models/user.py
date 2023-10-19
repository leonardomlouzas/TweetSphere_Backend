from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from tweetsphere.security import HashedPassword

if TYPE_CHECKING:
    from tweetsphere.models.post import Post


class User(SQLModel, table=True):
    """Represents the User model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    # It populates the .user attribute on the Post Model
    posts: List["Post"] = Relationship(back_populates="user")
