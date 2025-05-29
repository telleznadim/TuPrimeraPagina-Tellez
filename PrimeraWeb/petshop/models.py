from django.db import models


class Customer(models.Model):
    name = models.CharField("Nombre", max_length=100)
    email = models.EmailField("Correo electrónico", unique=True)
    phone = models.CharField("Teléfono", max_length=20)
    address = models.TextField("Dirección")

    def __str__(self):
        return self.name


class Pet(models.Model):
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='pets', verbose_name='Cliente')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    species = models.CharField(max_length=50, verbose_name='Especie')
    breed = models.CharField(max_length=50, blank=True, verbose_name='Raza')
    age = models.IntegerField(verbose_name='Edad')
    notes = models.TextField(blank=True, verbose_name='Notas')

    def __str__(self):
        return f"{self.name} ({self.species})"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    date = models.DateTimeField("Fecha", auto_now_add=True)
    total_amount = models.DecimalField(
        "Valor Total", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden #{self.id} - {self.customer.name} - {self.date.strftime('%Y-%m-%d')}"
