# Generated by Django 5.2.1 on 2025-05-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
