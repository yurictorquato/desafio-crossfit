from typing import Annotated

from contrib.schemas import BaseSchema
from pydantic import Field


class Categoria(BaseSchema):
    """"""

    nome: Annotated[
        str,
        Field(description="Nome da Categoria", examples="Foundations", max_length=15),
    ]
