from django.urls import path

from .views import typography_view


urlpatterns = [
    path('basic_typography', typography_view),
]