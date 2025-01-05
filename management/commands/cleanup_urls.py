from django.core.management.base import BaseCommand
from shortener_core.cron import cleanup_expired_urls

class Command(BaseCommand):
    help = 'Manually run the cleanup of expired URLs'

    def handle(self, *args, **kwargs):
        result = cleanup_expired_urls()
        print(result)