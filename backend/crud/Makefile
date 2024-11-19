# Variáveis
ENV = .env
PYTHON = python
PIP = pip
UVICORN = uvicorn
APP = app.main:app
DB_INIT_CMD = -c "from app.db.base import Base; from app.db.database import engine; from app.db.observation_model import Observation; Base.metadata.create_all(bind=engine)"

# Regras
.PHONY: help install run db-init clean format lint

help: ## Exibe as opções do Makefile
	@echo ""
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""

install: ## Instala as dependências do projeto
	$(PIP) install -r requirements.txt

run: ## Inicia o servidor FastAPI com Uvicorn
	$(UVICORN) $(APP) --reload

db-init: ## Inicializa o banco de dados
	$(PYTHON) $(DB_INIT_CMD)

clean: ## Remove arquivos de cache e temporários
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

format: ## Formata o código com black
	black .

lint: ## Verifica o código com flake8
	flake8 .
