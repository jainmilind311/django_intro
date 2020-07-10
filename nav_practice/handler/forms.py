from django import forms
from handler.models import Customer


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'nickname' : forms.TextInput(attrs={
                'class': 'form-control'
            }), 

            'fav_dish' : forms.TextInput(attrs={
                'class': 'form-control'
            }), 

            'contact_no' : forms.TextInput(attrs={
                'class': 'form-control'
            }), 

            'email' : forms.EmailInput(attrs={
                'class': 'form-control'
            }), 

        }
