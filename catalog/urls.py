from django.urls import re_path

from catalog import views

urlpatterns = [
    re_path('', views.home, name='home'),
    re_path('about', views.about, name='about'),
    re_path('contacts', views.contacts, name='contacts'),
    re_path('catalog', views.catalog, name='catalog'),
]
