from django import forms
from .models import *

class chaSeDaeForm(forms.ModelForm):
    class Meta:
        model = ChaSeDae
        fields = '__all__'
    date = forms.DateField(label='date', widget=forms.SelectDateWidget)
    
class nanoForm(forms.ModelForm):
    class Meta:
        model = Nano
        fields = '__all__'
    date = forms.DateField(label='date', widget=forms.SelectDateWidget)
        
class RDBForm(forms.ModelForm):
    class Meta:
        model = RDB
        fields = '__all__'
    date = forms.DateField(label='date', widget=forms.SelectDateWidget)
    
class tableForm(forms.ModelForm):
    class Meta:
        model = MenuTable
        fields = '__all__'
    date = forms.DateField(label='date', widget=forms.SelectDateWidget)