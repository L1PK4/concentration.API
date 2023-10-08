from pydantic import Field

from .base import BaseSchema


class IdSchema(BaseSchema):
    id: int = Field(..., title="Идентификатор")
