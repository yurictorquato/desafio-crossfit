from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException
from pydantic import UUID4
from sqlalchemy import select
from starlette import status

from app.centro_treinamento.models import CentroTreinamentoModel
from app.centro_treinamento.schemas import CentroTreinamentoRequest, CentroTreinamentoResponse
from app.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    path="/",
    summary="Cria um novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoResponse,
)
async def post(db_session: DatabaseDependency,
               centro_treinamento_request: CentroTreinamentoRequest = Body(...)) -> CentroTreinamentoResponse:
    centro_treinamento_response = CentroTreinamentoResponse(id=uuid4(), **centro_treinamento_request.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_response.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_response


@router.get(
    path="/",
    summary="Consulta todos os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoResponse],
)
async def get_all(db_session: DatabaseDependency) -> list[CentroTreinamentoResponse]:
    centros_treinamento = (
        await db_session.execute(select(CentroTreinamentoModel))
    ).scalars()

    return [
        CentroTreinamentoResponse.model_validate(centro_treinamento)
        for centro_treinamento in centros_treinamento
    ]


@router.get(
    path="/{id}",
    summary="Consulta um centro de treinamento pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoResponse,
)
async def get_by_id(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoResponse:
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel))).filter_by(
        id=id).scalar_one_or_none()

    if centro_treinamento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Centro de treinamento com ID {id} não encontrado.")

    return centro_treinamento
