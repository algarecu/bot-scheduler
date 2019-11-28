from celery.schedules import crontab


CELERY_IMPORTS = ('tasks.bot')
CELERY_TASK_RESULT_EXPIRES = 120
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'celery-bot-1-min': {
        'task': 'tasks.bot.start_bot',
        'schedule': crontab(minute="*")
    },
    'celery-bot-5-min': {
        'task': 'tasks.bot.start_bot',
        'schedule': crontab(minute='*/5')
    }
}