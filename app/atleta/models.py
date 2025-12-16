from __future__ import annotations

from datetime import datetime

from sqlalchemy import CHAR, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "tb_atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    altura: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    sexo: Mapped[str] = mapped_column(CHAR(length=1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("tb_categorias.pk_id"))
    centro_treinamento_id: Mapped[int] = mapped_column(
        ForeignKey("tb_centros_treinamento.pk_id")
    )

    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta", lazy="selectin")
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(
        back_populates="atleta",
        lazy="selectin"
    )
