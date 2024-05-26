from abc import ABC, abstractmethod
from typing import Any, Sequence

from pydantic import BaseModel


class BaseListSerializer[T: Sequence[Any], V: Sequence[BaseModel]](ABC):
    @abstractmethod
    def serialize_list(self, data: T) -> V:
        raise NotImplementedError
