from typing import Sequence

from pydantic import TypeAdapter
from sqlalchemy import RowMapping

from src.core.serializers.base import BaseListSerializer
from src.example.schemas.example_schema import ExampleSchema


example_adapter = TypeAdapter(list[ExampleSchema])


class ExampleSerializer(BaseListSerializer):
    def serialize_list(self, data: Sequence[RowMapping]) -> list[ExampleSchema]:
        return example_adapter.validate_python(data, from_attributes=True)