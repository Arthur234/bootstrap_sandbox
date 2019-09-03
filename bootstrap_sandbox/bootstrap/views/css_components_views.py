from django.shortcuts import render


def buttons_view(request):
    return render(request, 'css_components/buttons.html')


def navbar_view(request):
    return render(request, 'css_components/navbar.html')


def list_groups_and_badges_view(request):
    return render(request, 'css_components/list_groups_badges.html')


def forms_view(request):
    return render(request, 'css_components/forms.html')


def input_groups_view(request):
    return render(request, 'css_components/input_groups.html')


def alerts_and_progress_view(request):
    return render(request, 'css_components/alerts_progress.html')


def tables_and_pagination_view(request):
    return render(request, 'css_components/tables_pagination.html')


def cards_view(request):
    return render(request, 'css_components/cards.html')


def media_objects_view(request):
    return render(request, 'css_components/media_objects.html')


def jumbotron_view(request):
    return render(request, 'css_components/jumbotron.html')
