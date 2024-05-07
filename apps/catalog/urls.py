from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
