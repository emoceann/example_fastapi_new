from fastapi import APIRouter, Depends

from src.example.controller import ExampleController
from src.example.schemas.example_schema import ExampleSchema

router = APIRouter()


@router.get(
    "/data",
    response_model=list[ExampleSchema]
)
async def get_data(
        controller: ExampleController = Depends()
):
    return await controller.get_data_from_sources()