import asyncio

from fastapi import Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.config import get_session
from src.example.repositories.base import AbstractExampleRepo
from src.example.schemas.example_schema import ExampleSchema
from src.example.serializers.data_example_serializer import ExampleSerializer


class ExampleRepo(AbstractExampleRepo):
    def __init__(
            self,
            db_session: AsyncSession = Depends(get_session),
            serializer: ExampleSerializer = Depends()
    ):
        self.session = db_session
        self.serializer = serializer

    async def get_data_from_source(self, table_name: str) -> list[ExampleSchema]:
        stmt = select("*").select_from(text(table_name))
        try:
           async with asyncio.timeout(2):
                results = await self.session.execute(stmt)
        except TimeoutError:
            return []
        return self.serializer.serialize_list(results.mappings().all())
