from django import forms
from updater.models import Item


class TaskForm(forms.ModelForm):
    class Meta:
        model = Item
        field = '__all__'
        widgets = {
            'task' : forms.Textarea(attrs={
                'class' :'form-control'
            })
        }