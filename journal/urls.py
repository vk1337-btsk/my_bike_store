from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from journal.apps import JournalConfig
from journal.views import ArticleDetailView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView

app_name = JournalConfig.name

urlpatterns = \
    ([
         path('articles/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
         path('articles/create/', ArticleCreateView.as_view(), name='create_article'),
         path('articles/delete/<slug:slug>', ArticleDeleteView.as_view(), name='delete_article'),
         path('articles/edit/<slug:slug>', ArticleUpdateView.as_view(), name='update_article'),
     ]
     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
