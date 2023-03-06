release: python manage.py migrate --noinput && python manage.py collectstatic --no-input
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker backend.asgi:application