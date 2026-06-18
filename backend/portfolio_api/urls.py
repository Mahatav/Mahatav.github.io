from django.urls import path

from .views import health, portfolio

urlpatterns = [
    path("api/health/", health),
    path("api/portfolio/", portfolio),
]
