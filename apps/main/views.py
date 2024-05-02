from django.views.generic import TemplateView, ListView

from apps.journal.models import Articles


class HomeArticlesListView(ListView):
    template_name = 'main/home.html'
    model = Articles
    extra_context = {'title': 'Главная'}

    def get_queryset(self):
        return Articles.objects.filter(flag_publication=True).order_by('-count_views')


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'
    extra_context = {'title': 'Контакты'}


class AboutView(TemplateView):
    template_name = 'main/about.html'
    extra_context = {'title': 'О нас'}
