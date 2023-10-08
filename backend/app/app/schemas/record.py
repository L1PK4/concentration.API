from app.enums.record import MaterialType
from app.schemas.id_schema import IdSchema
from pydantic import Field

from .base import BaseSchema


class BaseRecord(BaseSchema):
    min_amount: int = Field(..., title="Минимальное количество")
    max_amount: int = Field(..., title="Максимальное количество")
    type: MaterialType = Field(
        ...,
        title="Тип материала",
        description="""
        Тип материала:  
        `iron` - железо;  
        `silicon` - кремний;  
        `aluminum` - алюминий;  
        `calcium` - кальций.  
        """,
    )
    created: int | None = Field(None, title="Дата создания")


class RecordCreate(BaseRecord):
    pass


class RecordUpdate(BaseRecord):
    min_amount: int | None = Field(None, title="Минимальное количество")
    max_amount: int | None = Field(None, title="Максимальное количество")
    type: MaterialType | None = Field(
        None,
        title="Тип материала",
        description="""
        Тип материала:  
        `iron` - железо;  
        `silicon` - кремний;  
        `aluminum` - алюминий;  
        `calcium` - кальций.  
        """,
    )


class RecordGet(IdSchema, BaseRecord):
    pass
