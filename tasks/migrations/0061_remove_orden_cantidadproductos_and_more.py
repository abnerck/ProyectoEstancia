# Generated by Django 4.2.5 on 2023-10-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0060_alter_orden_subtotalproductos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='cantidadProductos',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='precioUnitario',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='subtotalProductos',
        ),
    ]