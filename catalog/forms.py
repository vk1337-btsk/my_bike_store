from django import forms

from catalog.models import Version, Product


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
