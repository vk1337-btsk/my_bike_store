from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def about(request):
    return render(request, 'catalog/about.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')
