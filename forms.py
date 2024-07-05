from django import forms
from .models import LaptopFeature
class LaptopFeatureForm(forms.ModelForm):
    class Meta:
        model=LaptopFeature
        fields='__all__'
        exclude = ['predicted_price']
