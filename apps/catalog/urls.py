from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import CatalogListView, ProductDetailView, ProductUpdateView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
