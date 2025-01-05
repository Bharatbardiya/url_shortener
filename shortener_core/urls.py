
from django.urls import path
from .views import HomeView, URLRedirectView, URLExpiredView, UrlNotFound

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('expired/', URLExpiredView.as_view(), name='url_expired'),
    path('not-found/', UrlNotFound.as_view(), name='url_not_found'),
    path('<str:short_code>/', URLRedirectView.as_view(), name='redirect_url'),
]