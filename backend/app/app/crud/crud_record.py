from app.crud.base import CRUDBase
from app.models.record import Record
from app.schemas.record import RecordCreate, RecordUpdate


class CRUDRecord(CRUDBase[Record, RecordCreate, RecordUpdate]):
    pass


record = CRUDRecord(Record)
