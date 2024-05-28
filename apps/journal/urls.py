from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import never_cache

from apps.journal.apps import JournalConfig
from apps.journal.views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleCreateView, \
    ArticleDeleteView

app_name = JournalConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', never_cache(ArticleCreateView.as_view()), name='create_article'),
    path('articles/edit/<slug:slug>', never_cache(ArticleUpdateView.as_view()), name='update_article'),
    path('articles/delete/<slug:slug>', never_cache(ArticleDeleteView.as_view()), name='delete_article'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
