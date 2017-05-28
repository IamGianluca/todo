set -e

bash wait-for-it.sh --timeout=5 ${DB_NAME}:${DB_PORT}

python -s run.py
