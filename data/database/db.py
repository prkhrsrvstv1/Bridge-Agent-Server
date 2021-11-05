from abc import ABC, abstractmethod
from typing import Union, Generic, TypeVar, Any
from uuid import UUID

T = TypeVar("T")


class DB(ABC, Generic[T]):
    @abstractmethod
    def create(self, data: T) -> Union[T, str]:
        pass

    @abstractmethod
    def read(self, target_id: UUID) -> Union[T, str]:
        pass

    @abstractmethod
    def update(self, target_id: UUID, content: Any, strict: bool = True) -> Union[T, str]:
        pass

    @abstractmethod
    def delete(self, target_id: UUID) -> Union[T, str]:
        pass


class DictDB(DB, Generic[T]):
    def __init__(self):
        self._store = dict()

    def create(self, item: T) -> Union[T, str]:
        if item.id in self._store:
            return f"Failed to create. Item with id = {item.id} already exists."
        self._store[item.id] = item
        return item

    def read(self, target_id: UUID) -> Union[T, str]:
        item = self._store.get(target_id, None)
        if item is None:
            return f"Failed to read. Item with id = {target_id} doesn't exist."
        return item

    def update(self, target_id: UUID, content: Any, strict: bool = True) -> Union[T, str]:
        item = self.read(target_id)
        if type(item) is str:
            if strict:
                return f"Failed to update. Item with id = {target_id} doesn't exist."
            else:
                item = self.create(T(content=content))
        else:
            item.content = content
        return item

    def delete(self, target_id: UUID, strict: bool = True) -> Union[T, str]:
        item = self.read(target_id)
        if type(item) is str:
            if strict:
                return f"Failed to delete. Item with id = {target_id} doesn't exist."
        del self._store[target_id]
        return item
