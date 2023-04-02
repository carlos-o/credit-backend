from celery import shared_task
from .notifications import send_email
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_notification(email: str):
    """
        send email with the appoved credit


        :param email: email of the winner
        :type email: str
        :return: True
    """
    logger.info("OPEN: prepare to send mail")
    msg = "The credit has been registered successfully"
    send_email(email_address=email, message=msg)
    logger.info("CLOSE: email has been send correctly")
    return True
