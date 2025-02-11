#!/bin/sh
set -e

# Run database migrations
echo 'Applying migrations...'
python manage.py migrate

# Execute the main container command
exec "$@"
