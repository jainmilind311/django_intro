from django import forms
from input_form import models




class MyForm(forms.ModelForm):
    
    class Meta:
        model = models.User
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': 'form-control'
            }), 

            'email' : forms.EmailInput(attrs={
                'class': 'form-control'
            }), 

            'comments' : forms.Textarea(attrs={
                'class': 'form-control'
            }), 

        }
       