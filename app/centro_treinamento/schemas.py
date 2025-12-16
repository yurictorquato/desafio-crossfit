from typing import Annotated

from app.contrib.schemas import BaseSchema
from pydantic import UUID4, Field


class CentroTreinamentoRequest(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            examples=[
                "CrossFit Alcateia Arena",
            ],
            max_length=50,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do Centro de Treinamento",
            examples=[
                "Alameda Pádua, 238 - Pituba, Salvador - BA",
            ],
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Nome do Proprietário do Centro de Treinamento",
            examples=[
                "Renato Cariani",
            ],
            max_length=30,
        ),
    ]


class CentroTreinamentoResponse(CentroTreinamentoRequest):
    id: Annotated[UUID4, Field(description="Identificador do Centro de Treinamento")]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do centro de treinamento", examples=["CrossFit Alcateia Arena", ], max_length=50)]
