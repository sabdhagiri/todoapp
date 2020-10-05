#!/bin/bash

if [ $DEPLOY_ENVIRONMENT == 'DEVELOPMENT' ]
then
    for val in `cat .env.dev`; do export $val; done
elif [ $DEPLOY_ENVIRONMENT == 'PRODUCTION']
then
    for val in `cat .env.prod`; do export $val; done
fi


echo "Run database migrations..."
python manage.py db migrate

echo "Upgrde dbatabase to latest version..."
python manage.py db upgrade

echo "Starting App..."
python app.py