from datetime import datetime
from typing import TYPE_CHECKING

from app.db.base_class import Base
from app.enums.record import MaterialType
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.user import User


class Record(Base):
    id: int = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime, index=True, nullable=False,
                     default=datetime.utcnow)
    type: MaterialType = Column(
        ENUM(MaterialType),
        index=True,
        nullable=False
    )
    min_amount: int = Column(Integer, index=True, nullable=False)
    max_amount: int = Column(Integer, index=True, nullable=False)

    user_id: int = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), index=True, nullable=False)

    user: "User" = relationship(
        "User",
        back_populates="records",
    )
