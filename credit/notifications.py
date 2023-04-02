from django.core.mail.message import EmailMultiAlternatives
from src import settings


def send_email(email_address: str, message: str) -> bool:
    """
        This method get the data information and send a email with the template indicate.

        :param email_address: email to send information.
        :type email_address: string.
        :param message: message to sent.
        :type message: string.
    """
    subject = "New Credit"
    to = email_address
    from_email = settings.EMAIL_HOST_USER
    send = EmailMultiAlternatives(subject, message, from_email, [to],
                                  headers={'From': 'Credit <' + from_email + '>',
                                           'Reply-to': 'Credit <' + from_email + '>'})
    send.send()
    return True

