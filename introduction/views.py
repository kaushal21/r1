from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'introduction/index.html')


def aboutUs(request):
    return render(request, 'introduction/about.html')


def services(request):
    return render(request, 'introduction/services.html')

