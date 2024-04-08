from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    context = {'title': 'Главная'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)


def about(request):
    context = {'title': 'О нас'}
    return render(request, 'catalog/about.html', context)


def catalog(request):
    context = {'title': 'Каталог'}

    data = {'objects_list': Product.objects.all()}
    context.update(data)

    return render(request, 'catalog/catalog.html', context)


def product(request, pk):
    context = {
        'title': 'Продукт',
        'object': Product.objects.get(pk=pk)
    }

    return render(request, 'catalog/product.html', context)
