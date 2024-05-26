import pytest

from src.example.controller import ExampleController
from src.example.schemas.example_schema import ExampleSchema
from src.example.serializers.data_example_serializer import ExampleSerializer
from tests.example_module.mock_data import SlowMockSessionAlchemy, DataMockSessionResult, DataMockRepoSuccessful, SomeDataMockRepoSuccessful
from src.example.repositories.example_repo import ExampleRepo



class TestExampleRepo:
    async def test_example_repo_slow_session(self):
        repo = ExampleRepo(db_session=SlowMockSessionAlchemy())
        result = await repo.get_data_from_source("example")
        assert result == []

    async def test_example_repo_success(self):
        repo = ExampleRepo(
            db_session=DataMockSessionResult(),
            serializer=ExampleSerializer()
        )
        result = await repo.get_data_from_source("example")
        assert len(result) == 5
        assert all([isinstance(i, ExampleSchema) for i in result])


class TestExampleController:
    async def test_successful_data(self):
        controller = ExampleController(
            example_repo=DataMockRepoSuccessful()
        )
        result = await controller.get_data_from_sources()
        assert len(result) == 15
        assert all([isinstance(i, ExampleSchema) for i in result])
        assert result[0].id == 1 and result[-1].id == 15

    async def test_some_successful_data(self):
        controller = ExampleController(
            example_repo=SomeDataMockRepoSuccessful()
        )
        result = await controller.get_data_from_sources()
        assert len(result) == 10
        assert all([isinstance(i, ExampleSchema) for i in result])
        assert result[0].id == 1 and result[-1].id == 10

