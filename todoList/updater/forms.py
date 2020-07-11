from django import forms
from updater.models import Item


class TaskForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'task' : forms.TextInput(attrs={
                'class' :'form-control'
            }), 
            'date' : forms.DateInput(attrs={
                'class' : 'form-control', 
                'type': 'date'
            })
        }