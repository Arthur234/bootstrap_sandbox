from django.shortcuts import render


# Create your views here.
def typography_view(request):
    return render(request, 'basic_typography.html')
