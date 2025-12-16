from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, status, Body, HTTPException
from pydantic import UUID4
from sqlalchemy import select

from app.atleta.models import AtletaModel
from app.atleta.schemas import AtletaRequest, AtletaResponse, AtletaUpdate
from app.categoria.models import CategoriaModel
from app.centro_treinamento.models import CentroTreinamentoModel
from app.contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    path="/",
    summary="Cria um novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaResponse,
)
async def post(
    db_session: DatabaseDependency, atleta_request: AtletaRequest = Body(...)
) -> AtletaResponse:
    categoria_nome = atleta_request.categoria.nome

    categoria = (
        await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))
    ).scalar_one_or_none()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A categoria {categoria_nome} não foi encontrada.",
        )

    centro_treinamento_nome = atleta_request.centro_treinamento.nome

    centro_treinamento = (
        await db_session.execute(
            select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome)
        )
    ).scalar_one_or_none()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O centro de treinamento {centro_treinamento_nome} não foi encontrado.",
        )

    try:
        atleta_model = AtletaModel(
            id=uuid4(),
            created_at=datetime.now(timezone.utc),
            categoria_id=categoria.pk_id,
            centro_treinamento_id=centro_treinamento.pk_id,
            **atleta_request.model_dump(exclude={"categoria", "centro_treinamento"}),
        )

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro ao inserir os dados no banco.",
        )

    return AtletaResponse(
        id=atleta_model.id,
        created_at=atleta_model.created_at,
        categoria=categoria.nome,
        centro_treinamento=centro_treinamento.nome,
        **atleta_request.model_dump(exclude={"categoria", "centro_treinamento"}),
    )


@router.get(
    path="/",
    summary="Consulta todos os atletas.",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaResponse],
)
async def get_all(db_session: DatabaseDependency) -> list[AtletaResponse]:
    atletas = (await db_session.execute(select(AtletaModel))).scalars()

    return [AtletaResponse.model_validate(atleta) for atleta in atletas]


@router.get(
    path="/{id}",
    summary="Consulta um atleta pelo ID.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaResponse,
)
async def get_by_id(id: UUID4, db_session: DatabaseDependency) -> AtletaResponse:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalar_one_or_none()

    if atleta is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta com ID {id} não encontrado.",
        )

    return atleta


@router.patch(
    path="/{id}",
    summary="Edita um atleta pelo ID.",
    status_code=status.HTTP_200_OK,
    response_model=AtletaResponse,
)
async def update_by_id(
    id: UUID4, db_session: DatabaseDependency, atleta_update: AtletaUpdate = Body(...)
) -> AtletaResponse:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalar_one_or_none()

    if atleta is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta com ID {id} não encontrado.",
        )

    atleta_update = atleta_update.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return atleta


@router.delete(
    path="/{id}",
    summary="Deleta um atleta pelo ID.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_by_id(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalar_one_or_none()

    if atleta is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta com ID {id} não encontrado."
        )

    await db_session.delete(atleta)
    await db_session.commit()
