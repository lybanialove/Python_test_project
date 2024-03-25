from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Event(Base):
    __tablename__ = "event"
    
    id: Mapped[int] = mapped_column(primary_key = True, index = True)  
    name: Mapped[str] = mapped_column(nullable=False)
    start_at: Mapped[datetime] = mapped_column(default=func.now())
    paticipants: Mapped[list["User"] | None] = relationship(
        back_populates = "events",
        secondary="user_event"
    )
    description: Mapped[str] 
    uniq_code: Mapped[str] = mapped_column(nullable=False)

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] =  mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    events: Mapped[list["Event"] | None] = relationship(
        back_populates = "paticipants",
        secondary="user_event"
    )
    password: Mapped[str] = mapped_column(nullable=False)

class UserEvent(Base):
    __tablename__ = "user_event"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey("event.id", ondelete="CASCADE"),
        primary_key=True,
    )

    details: Mapped[str | None]