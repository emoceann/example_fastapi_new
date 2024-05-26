import asyncio
from itertools import chain

from fastapi import Depends

from src.example.repositories.example_repo import ExampleRepo
from src.example.schemas.example_schema import ExampleSchema


class ExampleController:
    def __init__(
            self,
            example_repo: ExampleRepo = Depends()
    ):
        self.example_repo = example_repo
        self.first_table_example = "data_first"
        self.second_table_example = "data_second"
        self.third_table_example = "data_third"

    async def get_data_from_sources(self) -> list[ExampleSchema]:
        result = await asyncio.gather(
            self.example_repo.get_data_from_source(self.first_table_example),
            self.example_repo.get_data_from_source(self.second_table_example),
            self.example_repo.get_data_from_source(self.third_table_example),
        )
        sorted_result = sorted(chain.from_iterable(result), key=lambda data: data.id)
        return sorted_result
