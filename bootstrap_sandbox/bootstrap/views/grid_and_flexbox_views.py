from django.shortcuts import render


def grid_system_view(request):
    return render(request, 'grid_and_flexbox/grid_system.html')


def grid_alignment_view(request):
    return render(request, 'grid_and_flexbox/grid_alignment.html')


def flexbox_view(request):
    return render(request, 'grid_and_flexbox/flexbox.html')


def auto_margins_and_wrap_view(request):
    return render(request, 'grid_and_flexbox/auto_margins_wrapping_order.html')
