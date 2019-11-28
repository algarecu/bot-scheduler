BOT MANAGER
===========

* Add your master script for the bot with execution workflow.
* In different windows do the following:
  * celery beat -A app.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidle=/tmp/celerybeat.pid
  * celery worker -A app.celery --concurrency=0 --loglevel=DEBUG -f celery.log
  * tail -f celery.log
