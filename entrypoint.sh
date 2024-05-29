#!/bin/sh
echo ENV $ENVIRONMENT
echo VERSION $VERSION
env >> /etc/environment
echo Starting the app
cd app
mkdir -p logs
exec python api.py