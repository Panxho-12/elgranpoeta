
from django import forms
from libros.models import Libros

class FormLibros(forms.ModelForm):
    class Meta:
        model = Libros
        fields = '__all__'
        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
        }
