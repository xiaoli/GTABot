# GPTarXBot

## Commands

### Grab papers from arXiv
heroku run python manage.py grabpapers

## Example env_example
env_example:
export TELEGRAM_API_TOKEN='{AAA:BBB}'
export TELEGRAM_CHANNEL_ID=-100{CHANNEL_ID}
export ARXIV_HOST_URL='https://arxiv.org'
export ENABLE_TELEGRAM_CHANNEL_MSG=True

## Local .env file
heroku config:get CONFIG-VAR-NAME -s  >> .env
source .env

## Heroku Scheduler
https://devcenter.heroku.com/articles/scheduler

## Heroku Log
https://devcenter.heroku.com/articles/logging

heroku logs --tail