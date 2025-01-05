from django.contrib import admin

# Register your models here.
from shortener_core.models import URL

admin.site.register(URL)
