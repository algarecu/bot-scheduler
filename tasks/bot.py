import celery
import os


@celery.task()
def print_hello():
    logger = print_hello.get_logger()
    logger.info("Hello")

@celery.task()
def start_bot():
    logger = start_bot.get_logger()
    logger.info("Creating bot...")
    dirpath = os.getcwd()
    cmd = dirpath + "/tasks/bot.sh"
    os.system(cmd)

