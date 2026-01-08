# Desafio CrossFit

API REST para gerenciamento de atletas e treinos de CrossFit.

## Tecnologias

- Python 3.12+
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL
- Docker

## Como Executar

### Com Docker

```bash
# Subir containers
docker-compose up -d

# Rodar migrações
docker-compose exec app alembic upgrade head
```

### Local

```bash
# Instalar dependências
uv sync

# Ativar ambiente virtual
source .venv/bin/activate

# Rodar migrações
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

## Acesso

- API: http://localhost:8000
- Documentação: http://localhost:8000/docs

## Estrutura

```
app/
├── api/         # Endpoints
├── models/      # Modelos do banco
├── schemas/     # Validação
└── main.py      # Aplicação
```

## Autor

Yuri Torquato - [@yurictorquato](https://github.com/yurictorquato)
