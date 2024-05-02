from django.urls import reverse
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from apps.journal.forms import ArticleForm
from apps.journal.models import Articles


class ArticleDetailView(DetailView):
    model = Articles
    extra_context = {'title': 'Статья'}

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.count_views += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Articles
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('journal:article_detail', kwargs={'slug': self.object.slug})


class ArticleUpdateView(UpdateView):
    model = Articles
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('journal:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(DeleteView):
    model = Articles
    fields = ('title', 'text', 'image', 'flag_publication',)

    def get_success_url(self):
        return reverse('main:home')
