from typing import Annotated, Optional

from pydantic import Field, PositiveFloat, PositiveInt

from app.categoria.schemas import CategoriaRequest
from app.centro_treinamento.schemas import CentroTreinamentoAtleta
from app.contrib.schemas import BaseSchema, ResponseMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do Atleta", examples=["Yuri", ], max_length=50)
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do Atleta",
            examples=["37422715553", ],
            pattern=r"^\d{11}$",
            min_length=11,
            max_length=11,
        ),
    ]
    idade: Annotated[PositiveInt, Field(description="Idade do Atleta", examples=[25, ])]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=[75.5, ])]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do Atleta", examples=[1.77, ])
    ]
    sexo: Annotated[
        str,
        Field(
            description="Sexo do Atleta (M ou F)",
            examples=["M", ],
            pattern="^[MF]$",
            min_length=1,
            max_length=1,
        ),
    ]
    categoria: Annotated[CategoriaRequest, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de Treinamento do atleta")]


class AtletaRequest(Atleta):
    pass


class AtletaResponse(Atleta, ResponseMixin):
    pass


class AtletaUpdate(BaseSchema):
    idade: Annotated[Optional[PositiveInt], Field(None, description="Idade do Atleta", examples=[18, ])]
    peso: Annotated[Optional[PositiveFloat], Field(None, description="Peso do Atleta", examples=[90.5, ])]
