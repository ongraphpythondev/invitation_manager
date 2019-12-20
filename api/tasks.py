# Django Imports
from celery import task
from django.core.mail import send_mail
from django.conf import settings


@task
def celery_mail_generation(receiver):
    """
    Task to send an e-mail notification using celery.
    """
    subject = "Invitation"
    message = "You are invited."
    sender = settings.EMAIL_HOST_USER
    mail_sent = send_mail(subject, message, sender, [receiver])
    return mail_sent
