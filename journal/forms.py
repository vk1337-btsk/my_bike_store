from django import forms

from journal.models import Articles


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ArticleForm(StyleForMixin, forms.ModelForm):

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Articles
        fields = ('title', 'text', 'image', 'flag_publication')

    def clean_title(self):
        clean_title = self.cleaned_data['title']
        for word in self.forbidden_words:
            if word in clean_title.lower():
                raise forms.ValidationError(f'Название статьи не может содержать слово "{word}"')
        return clean_title

    def clean_text(self):
        clean_text = self.cleaned_data['text']
        for word in self.forbidden_words:
            if word in clean_text.lower():
                raise forms.ValidationError(f'Текст статьи не может содержать слово "{word}"')
        return clean_text
