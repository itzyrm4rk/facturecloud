# FactureCloud : Module 0

Trois microservices Flask : api-factures, service-calcul, service-notifications.

## Installation
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
pip install flask gunicorn pytest

## Tests
python -m pytest -v

## Lancer les services
cd service-calcul && PORT=8081 python main.py
cd service-notifications && PORT=8082 python main.py
cd api-factures && PORT=8080 python main.py
