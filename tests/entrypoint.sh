set -e

bash wait-for-it.sh --timeout=5 ${DB_NAME}:${DB_PORT}
bash wait-for-it.sh --timeout=5 ${API_HOST}:${API_PORT}

pytest --cov=todo
