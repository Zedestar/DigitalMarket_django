from django import forms
from .models import Product

# - Creating the forms here 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [""]