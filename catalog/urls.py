from django.urls import path

from app_main.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
]
