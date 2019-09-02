from django.shortcuts import render


def typography_view(request):
    return render(request, 'utilities/basic_typography.html')


def text_alignment_display_view(request):
    return render(request, 'utilities/text_alignment_display.html')
