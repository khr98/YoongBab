from django import forms
from .models import *

class MenuForm(forms.ModelForm):
    class Meta:
        model = ChaSeDae
        fields = '__all__'