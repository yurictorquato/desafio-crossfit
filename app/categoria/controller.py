from __future__ import annotations

from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from starlette import status

from app.categoria.models import CategoriaModel
from app.categoria.schemas import CategoriaResponse, CategoriaRequest
from app.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    path="/",
    summary="Cria uma nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaResponse,
)
async def post(db_session: "DatabaseDependency",
               categoria_request: "CategoriaRequest" = Body(...)) -> "CategoriaResponse":
    categoria_response = CategoriaResponse(id=uuid4(), **categoria_request.model_dump())
    categoria_model = CategoriaModel(**categoria_response.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_response


@router.get(
    path="/",
    summary="Consulta todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaResponse],
)
async def get_all(db_session: "DatabaseDependency") -> list["CategoriaResponse"]:
    categorias_model = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return [
        CategoriaResponse.model_validate(model)
        for model in categorias_model
    ]


@router.get(
    path="/{id}",
    summary="Consulta uma categoria pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaResponse,
)
async def get_by_id(id: UUID4, db_session: "DatabaseDependency") -> "CategoriaResponse":
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalar_one_or_none()

    if categoria is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria com ID {id} não encontrada.")

    return categoria
