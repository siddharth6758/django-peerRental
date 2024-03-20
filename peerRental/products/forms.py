from django import forms
from products.models import *

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['prod_img','description','prod_price','rent_type','title']