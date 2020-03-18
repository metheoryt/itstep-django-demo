from django.core.signals import request_finished, request_started
import logging
import time

log = logging.getLogger(__name__)


@request_started.connect
def fix_time_start(sender, **kwargs):
    log.info('request started')


@request_finished.connect
def log_request_finish(sender, **kwargs):
    log.info('request finished')
