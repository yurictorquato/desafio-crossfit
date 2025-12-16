from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.atleta.models import AtletaModel
from app.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = "tb_categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)

    atleta: Mapped[list["AtletaModel"]] = relationship(back_populates="categoria")
