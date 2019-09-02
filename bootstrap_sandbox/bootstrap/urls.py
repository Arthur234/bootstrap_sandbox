from django.urls import path

from .views import (
    typography_view, text_alignment_display_view
)


urlpatterns = [

    # utilities
    path('basic_typography', typography_view, name='basic_typography'),
    path('text_alignment_display', text_alignment_display_view, name='text_alignment_display'),

]
