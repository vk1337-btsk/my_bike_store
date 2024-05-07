from django import forms
from django.forms import BooleanField

from apps.catalog.models import Version, Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product', )


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        clean_name = self.cleaned_data['name']
        for word in self.forbidden_words:
            if word in clean_name.lower():
                raise forms.ValidationError(f'Название продукта не может содержать слово "{word}"')
        return clean_name

    def clean_description(self):
        clean_description = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in clean_description.lower():
                raise forms.ValidationError(f'Описание продукта не может содержать слово "{word}"')
        return clean_description
