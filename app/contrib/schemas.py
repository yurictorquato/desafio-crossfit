from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, UUID4, Field


class BaseSchema(BaseModel):
    model_config = {
        "extra": "forbid",
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }


class ResponseMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de Criação")]
