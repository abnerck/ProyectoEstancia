# Generated by Django 4.2.5 on 2023-11-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0089_compra_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='productos',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
