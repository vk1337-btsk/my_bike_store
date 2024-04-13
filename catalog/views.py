from django.views.generic import ListView, DetailView
from catalog.models import Product


class CatalogListView(ListView):
    template_name = 'catalog/catalog.html'
    model = Product
    context_object_name = 'objects_list'
    paginate_by = 2
    extra_context = {'title': 'Каталог'}


class ProductDetailView(DetailView):
    template_name = 'catalog/product.html'
    model = Product
