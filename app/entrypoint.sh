set -e

bash wait-for-it.sh --timeout=5 db:5432

python run.py
