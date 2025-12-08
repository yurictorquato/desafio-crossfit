from typing import Annotated

from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat, PositiveInt


class Atleta(BaseSchema):
    """"""

    nome: Annotated[
        str, Field(description="Nome do Atleta", examples="Yuri", max_length=50)
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do Atleta",
            examples="37422715553",
            pattern=r"^\d{11}$",
            min_length=11,
            max_length=11,
        ),
    ]
    idade: Annotated[PositiveInt, Field(description="Idade do Atleta", examples=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", examples=75.5)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do Atleta", examples=1.77)
    ]
    sexo: Annotated[
        str,
        Field(
            description="Sexo do Atleta (M ou F)",
            examples="M",
            pattern="^[MF]$",
            min_length=1,
            max_length=1,
        ),
    ]
