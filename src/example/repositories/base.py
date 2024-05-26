from abc import ABC, abstractmethod

from src.example.schemas.example_schema import ExampleSchema


class AbstractExampleRepo(ABC):
    @abstractmethod
    async def get_data_from_source(self, table_name: str) -> list[ExampleSchema]:
        raise NotImplementedError
