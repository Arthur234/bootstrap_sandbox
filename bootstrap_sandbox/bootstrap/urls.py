from django.urls import path

from .views.utilities_views import *
from .views.css_components_views import *
from .views.grid_and_flexbox_views import *
from .views.javascript_widgets import *

urlpatterns = [

    # utilities
    path('basic_typography', typography_view, name='basic_typography'),
    path('text_alignment_display', text_alignment_display_view, name='text_alignment_display'),
    path('floats_and_position', floats_and_position_view, name='floats_and_position'),
    path('color_and_background', color_and_background_view, name='colors_and_background'),
    path('spacing', spacing_view, name='spacing'),
    path('sizing', sizing_view, name='sizing'),
    path('breakpoints', breakpoints_view, name='breakpoints'),

    # css_components
    path('buttons', buttons_view, name='buttons'),
    path('navbar', navbar_view, name='navbar'),
    path('list_groups_and_badges', list_groups_and_badges_view, name='list_groups_and_badges'),
    path('forms', forms_view, name='forms'),
    path('input_groups', input_groups_view, name='input_groups'),
    path('alerts_and_progress', alerts_and_progress_view, name='alerts_and_progress'),
    path('tables_and_pagination', tables_and_pagination_view, name='tables_and_pagination'),
    path('cards', cards_view, name='cards'),
    path('media_objects', media_objects_view, name='media_objects'),
    path('jumbotron', jumbotron_view, name='jumbotron'),

    # grid & flexbox
    path('grid_system', grid_system_view, name='grid_system'),
    path('grid_alignment', grid_alignment_view, name='grid_alignment'),
    path('flexbox', flexbox_view, name='flexbox'),
    path('auto_margins_and_wrap', auto_margins_and_wrap_view, name='auto_margins_and_wrap'),

    # javascript widgets
    path('carousel', carousel_view, name='carousel'),
    path('collapse', collapse_view, name='collapse'),
    path('tooltips', tooltips_view, name='tooltips'),
    path('popevers', popevers_view, name='popevers'),
    path('modals', modals_view, name='modals'),
    path('scrollspy', scrollspy_view, name='scrollspy'),

]
