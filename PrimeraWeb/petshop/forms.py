from django import forms
from .models import Pet, Customer, Order


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['customer', 'name', 'species', 'breed', 'age', 'notes']
        # fields = '__all__'
        # labels = {
        #     'customer': 'Cliente',
        #     'name': 'Nombre',
        #     'species': 'Especie',
        #     'breed': 'Raza',
        #     'age': 'Edad',
        #     'notes': 'Notas',
        # }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_amount']
