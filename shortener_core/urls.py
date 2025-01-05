# url_app/urls.py
from django.urls import path
from .views import HomeView, URLRedirectView, URLExpiredView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('expired/', URLExpiredView.as_view(), name='url_expired'),
    path('<str:short_code>/', URLRedirectView.as_view(), name='redirect_url'),
]