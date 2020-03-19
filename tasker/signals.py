from django.core.signals import request_finished, request_started
from django.dispatch import receiver
import logging

log = logging.getLogger(__name__)


@receiver(request_started)
def log_request_start(sender, **kwargs):
    log.info('request started')


@receiver(request_finished)
def log_request_finish(sender, **kwargs):
    log.info('request finished')
