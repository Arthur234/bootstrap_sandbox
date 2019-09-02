from django.shortcuts import render


def carousel_view(request):
    return render(request, 'javascript_widgets/carousel.html')


def collapse_view(request):
    return render(request, 'javascript_widgets/collapse.html')


def tooltips_view(request):
    return render(request, 'javascript_widgets/tooltips.html')


def popevers_view(request):
    return render(request, 'javascript_widgets/popovers.html')


def modals_view(request):
    return render(request, 'javascript_widgets/modals.html')


def scrollspy_view(request):
    return render(request, 'javascript_widgets/scrollspy.html')
