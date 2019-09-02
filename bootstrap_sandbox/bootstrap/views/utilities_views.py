from django.shortcuts import render


def typography_view(request):
    return render(request, 'utilities/basic_typography.html')


def text_alignment_display_view(request):
    return render(request, 'utilities/text_alignment_display.html')


def floats_and_position_view(request):
    return render(request, 'utilities/floats_position.html')


def color_and_background_view(request):
    return render(request, 'utilities/colors_background.html')


def spacing_view(request):
    return render(request, 'utilities/spacing.html')


def sizing_view(request):
    return render(request, 'utilities/sizing.html')


def breakpoints_view(request):
    return render(request, 'utilities/breakpoints.html')
