from django import forms
from django.forms.widgets import EmailInput, TextInput

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        }
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Escribe tu e-mail'
        }
    ), min_length=3, max_length=100)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows':3,
            'placeholder': 'Escribe tu mensaje'

        }
    ),min_length=10, max_length=1000)