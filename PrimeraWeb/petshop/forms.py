from django import forms
from .models import Pet, Customer, Order


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['customer', 'name', 'species', 'breed', 'age', 'notes']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount']
