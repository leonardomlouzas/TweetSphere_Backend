from datetime import datetime
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from tweetsphere.security import User


class Post(SQLModel, table=True):
    """Represents the Post Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user_id: Optional[int] = Field(foreign_key="user.id")
    parent_id: Optional[int] = Field(foreign_key="post.id")

    # It populates a `.posts` attribute to the `User` model.
    user: Optional["User"] = Relationship(back_populates="posts")

    # It populates a `.replies` on this model.
    parent: Optional["Post"] = Relationship(
        back_populates="replies",
        sa_relationship_kwargs=dict(remote_side="Post.id"),
    )

    # This lists all children to this post
    replies: list["Post"] = Relationship(back_populates="parent")

    def __lt__(self, other):
        """This enables post.replies.sort() to sort by date"""
        return self.date < other.date
