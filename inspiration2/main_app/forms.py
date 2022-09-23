from django import forms
from django.forms import ModelForm
from .models import Note
from .models import Inspiration
from .models import Gallery


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, gallery):
        return "%s" % gallery.name

class AddGalleriesForm(forms.ModelForm):
    class Meta:
        model = Inspiration
        fields = ['name', 'description', 'link', 'galleries']
        name = forms.CharField(max_length=500)
        description = forms.CharField(max_length=1000)
        link = forms.CharField(max_length=1000)
        galleries = forms.ModelMultipleChoiceField(
        queryset=Gallery.objects.values('name'),
        widget=forms.CheckboxSelectMultiple
        )

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['date', 'note']