from typing import Annotated

from pydantic import Field, UUID4

from app.contrib.schemas import BaseSchema


class CategoriaRequest(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Nome da Categoria", examples=["Foundations", ], max_length=15),
    ]


class CategoriaResponse(CategoriaRequest):
    id: Annotated[UUID4, Field(description="Identificador da Categoria")]
