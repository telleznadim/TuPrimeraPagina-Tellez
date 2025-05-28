from django.contrib import admin
from .models import Customer, Pet, Order

admin.site.register(Customer)
admin.site.register(Pet)
admin.site.register(Order)
