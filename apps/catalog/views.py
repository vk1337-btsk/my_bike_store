from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.forms import inlineformset_factory

from apps.catalog.forms import VersionForm, ProductForm
from apps.catalog.models import Product, Version, Category


class ProductListView(ListView):
    model = Product
    paginate_by = 4
    extra_context = {'title': 'Товары'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {"title": "Просмотр товара"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем объект Product, который отображается на странице
        product = self.get_object()
        # Получаем связанную с продуктом активную версию
        active_version = Version.objects.filter(product=product, is_active=True).first()
        # Добавляем информацию о версии в контекст страницы
        context['active_version'] = active_version
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {"title": "Редактирование товара"}

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {"title": "Создание товара"}
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Category.objects.all()
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    extra_context = {"title": "Удаление товара"}
    success_url = reverse_lazy('catalog:catalog')
