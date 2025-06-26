from django import forms
from base.models import Main_Kiyim

class ProductForm(forms.ModelForm):
    class Meta:
        model = Main_Kiyim
        fields = '__all__'
