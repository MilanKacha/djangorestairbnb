#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Checking"

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
        sleep 0.1
    done

    echo "The database is up and running :-D"
fi

# Run migrations
python manage.py makemigrations
python manage.py migrate

exec "$@"

# # Collect static files (optional, remove if not needed)
# echo "Collecting static files..."


# # Collect static files (optional, remove if not needed)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# # Start server
# echo "Starting server..."
# exec python manage.py runserver 0.0.0.0:8000