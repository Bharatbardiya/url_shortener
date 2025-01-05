from django.utils import timezone
from .models import URL
import logging

logger = logging.getLogger(__name__)

def cleanup_expired_urls():
    """
    Delete all expired URLs and log the cleanup operation
    """
    try:
        now = timezone.now()
        expired_urls = URL.objects.filter(expires_at__lt=now)
        count = expired_urls.count()
        expired_urls.delete()
        return "SUCCESS"
    except Exception as e:
        return "FAILURE"