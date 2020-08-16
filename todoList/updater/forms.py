from django import forms
from updater.models import Item, Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control ',
                'type': 'date'
            })
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note',)
        widgets = {
            'note': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
