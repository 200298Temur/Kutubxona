from django import forms
from django.utils.text import slugify

from .models import *


class AddAvtorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'photo','content']  # 'filelds' o'rniga 'fields'
        widgets = {
            'content': forms.Textarea(attrs={'cols': 69, 'rows': 10})
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name')
        if title and not cleaned_data.get('slug'):
            cleaned_data['slug'] = slugify(title)
        return cleaned_data
    
class AddKitobForm(forms.ModelForm):
    author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label="Boshqa Mualliflar",label="Muallif")

    class Meta:
        model=Kitob
        fields=['name','author','photo','file']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name')
        if title and not cleaned_data.get('slug'):
            cleaned_data['slug'] = slugify(title)
        return cleaned_data