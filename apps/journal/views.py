from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from apps.journal.forms import ArticleForm
from apps.journal.models import Articles


class ArticleListView(ListView):
    model = Articles
    extra_context = {'title': 'Статьи'}


class ArticleDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Articles
    extra_context = {'title': 'Статья'}

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.count_views += 1
        self.object.save()
        return self.object


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    permission_required = 'journal.add_articles'
    model = Articles
    form_class = ArticleForm
    extra_context = {"title": "Создание статьи"}

    def get_success_url(self):
        return reverse('journal:article_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    permission_required = 'journal.change_articles'
    model = Articles
    form_class = ArticleForm
    extra_context = {"title": "Редактирование статьи"}

    def get_success_url(self):
        return reverse('journal:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    permission_required = 'journal.delete_articles'
    model = Articles
    extra_context = {"title": "Удаление статьи"}
    success_url = reverse_lazy('main:home')
