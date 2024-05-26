import asyncio
import random
from typing import Optional, Any

from sqlalchemy import Executable, util
from sqlalchemy.engine.interfaces import _CoreAnyExecuteParams
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm._typing import OrmExecuteOptionsParameter
from sqlalchemy.orm.session import _BindArguments

from src.example.repositories.base import AbstractExampleRepo
from src.example.schemas.example_schema import ExampleSchema


class SlowMockSessionAlchemy(AsyncSession):
    async def execute(
        self,
        statement: Executable,
        params: Optional[_CoreAnyExecuteParams] = None,
        *,
        execution_options: OrmExecuteOptionsParameter = util.EMPTY_DICT,
        bind_arguments: Optional[_BindArguments] = None,
        **kw: Any,
    ) -> None:
        await asyncio.sleep(3)


class MockMappingsAlchemy:
    def mappings(self):
        return self

    def all(self):
        return [
            {"id": 1, "name": "Test_1"},
            {"id": 2, "name": "Test_2"},
            {"id": 3, "name": "Test_3"},
            {"id": 4, "name": "Test_4"},
            {"id": 5, "name": "Test_5"}
        ]


class DataMockSessionResult(AsyncSession):
    async def execute(
        self,
        statement: Executable,
        params: Optional[_CoreAnyExecuteParams] = None,
        *,
        execution_options: OrmExecuteOptionsParameter = util.EMPTY_DICT,
        bind_arguments: Optional[_BindArguments] = None,
        **kw: Any,
    ) -> MockMappingsAlchemy:
        return MockMappingsAlchemy()


class DataMockRepoSuccessful(AbstractExampleRepo):
    async def get_data_from_source(self, table_name: str):
        if table_name == "data_first":
            return [ExampleSchema(id=i, name=random.choice("abcdefg")) for i in range(1,6)]
        elif table_name == "data_second":
            return [ExampleSchema(id=i, name=random.choice("abcdefg")) for i in range(6,11)]
        return [ExampleSchema(id=i, name=random.choice("abcdefg")) for i in range(11,16)]

class SomeDataMockRepoSuccessful(AbstractExampleRepo):
    async def get_data_from_source(self, table_name: str):
        if table_name == "data_first":
            return [ExampleSchema(id=i, name=random.choice("abcdefg")) for i in range(1, 6)]
        elif table_name == "data_second":
            return [ExampleSchema(id=i, name=random.choice("abcdefg")) for i in range(6,11)]
        return []
