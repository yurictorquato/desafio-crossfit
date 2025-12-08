from typing import Annotated

from contrib.schemas import BaseSchema
from pydantic import Field


class CentroTreinamento(BaseSchema):
    """"""

    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            examples="CrossFit Alcateia Arena",
            max_length=30,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do Centro de Treinamento",
            examples="Alameda Pádua, 238 - Pituba, Salvador - BA",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Nome do Proprietário do Centro de Treinamento",
            examples="Renato Cariani",
            max_length=30,
        ),
    ]
