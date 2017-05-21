set -e

bash wait-for-it.sh --timeout=5 db:5432
bash wait-for-it.sh --timeout=5 app:5000

pytest --cov=todo
