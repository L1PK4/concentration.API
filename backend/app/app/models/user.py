from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.record import Record


class User(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean(), default=True)
    is_superuser: bool = Column(Boolean(), default=False)

    records: list["Record"] = relationship(
        "Record",
        back_populates="user",
        cascade="all, delete",
    )
