from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.apps import MainConfig
from main.views import HomeArticlesListView, ContactsView, AboutView

app_name = MainConfig.name

urlpatterns = ([
    path('', HomeArticlesListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

