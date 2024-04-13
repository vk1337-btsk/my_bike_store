from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = ([
                   path('catalog/', CatalogListView.as_view(), name='catalog'),
                   path('product/<int:pk>', ProductDetailView.as_view(), name='product_info'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
