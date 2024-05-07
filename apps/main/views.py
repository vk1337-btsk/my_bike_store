from django.views.generic import TemplateView

from apps.journal.models import Articles


class HomeArticlesListView(TemplateView):
    template_name = 'journal/articles_list.html'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Articles.objects.filter(flag_publication=True).order_by('-count_views')
        return context_data


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'
    extra_context = {'title': 'Контакты'}


class AboutView(TemplateView):
    template_name = 'main/about.html'
    extra_context = {'title': 'О нас'}
