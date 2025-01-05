
from django.db import models
from django.utils import timezone
import hashlib
import time

class URL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    access_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
    
    @classmethod
    def generate_short_code(cls, url):
        # Generate a unique code based on timestamp and URL
        timestamp = str(time.time()).encode('utf-8')
        url_bytes = url.encode('utf-8')
        hash_input = timestamp + url_bytes
        short_code = hashlib.sha256(hash_input).hexdigest()[:8]
        return short_code
    
    def increment_access_count(self):
        self.access_count += 1
        self.save()
    
    @property
    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False