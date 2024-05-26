from src.example.repositories.example_repo import ExampleRepo
from src.example.schemas.example_schema import ExampleSchema
from src.example.serializers.data_example_serializer import example_adapter
from tests.example_module.mock_data import SomeDataMockRepoSuccessful


class TestEndpointExample:
    async def test_get_data(self, client, prepare_db):
        resp = await client.get("/example/data")
        result = resp.json()
        assert len(result) == 60
        result = example_adapter.validate_python(result)
        assert all(isinstance(i, ExampleSchema) for i in result)
        assert result[0].id == 1 and result[-1].id == 60

    async def test_some_data(self, app, client):
        app.dependency_overrides[ExampleRepo] = SomeDataMockRepoSuccessful
        resp = await client.get("/example/data")
        result = resp.json()
        assert len(result) == 10
        result = example_adapter.validate_python(result)
        assert all(isinstance(i, ExampleSchema) for i in result)
        assert result[0].id == 1 and result[-1].id == 10