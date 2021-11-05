from data.model import Parcel
from typing import Union
from uuid import UUID


class DBHandler:
    def __init__(self, db_name: str, data_type: type):
        if db_name == "dict":
            from data.database.db import DictDB
            self._db = DictDB[data_type]()

    def create(self, parcel: Parcel) -> Union[Parcel, str]:
        return self._db.create(parcel)

    def read(self, target_id: UUID) -> Union[Parcel, str]:
        return self._db.read(target_id)

    def update(self, target_id: UUID, content: str, strict: bool = True) -> Union[Parcel, str]:
        return self._db.update(target_id, content, strict)

    def delete(self, target_id: UUID) -> Union[Parcel, str]:
        return self._db.delete(target_id)
