from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "photo"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full px-2 py-2 border border-gray-300 rounded-md focus:ring focus:ring-green-400", "placeholder": "Enter product name",  "style": "color: #9CA3AF; font-style: italic;"}),
            "description": forms.Textarea(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring focus:ring-green-400", "rows": 3, "placeholder": "Enter product description",  "style": "placeholder-color: #9CA3AF; font-style: italic;"}),
            "price": forms.NumberInput(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring focus:ring-green-400",  "placeholder": "Enter product price",  "style": "placeholder-color: #9CA3AF; font-style: italic;"}),
            "category": forms.Select(attrs={"class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring focus:ring-green-400"}),
            "photo": forms.FileInput(attrs={"class": "w-full border border-gray-300 rounded-md focus:ring focus:ring-green-400"}),
        }
