from sqlmodel import Field, SQLModel
from typing import Optional
from tweetsphere.security import HashedPassword


class User(SQLModel, table=True):
    """Represents the User model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword
