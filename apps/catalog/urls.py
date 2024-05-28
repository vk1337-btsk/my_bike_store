from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView, CategoryDetailView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/edit/<int:pk>', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/delete/<int:pk>', never_cache(ProductDeleteView.as_view()), name='product_delete'),

    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
