from django.urls import path

from .views.utilities_views import *


urlpatterns = [

    # utilities
    path('basic_typography', typography_view, name='basic_typography'),
    path('text_alignment_display', text_alignment_display_view, name='text_alignment_display'),
    path('floats_and_position', floats_and_position_view, name='floats_and_position'),
    path('color_and_background', color_and_background_view, name='color_and_background'),
    path('spacing', spacing_view, name='spacing'),
    path('sizing', sizing_view, name='sizing'),
    path('breakpoints', breakpoints_view, name='breakpoints'),

    # css_components
]
