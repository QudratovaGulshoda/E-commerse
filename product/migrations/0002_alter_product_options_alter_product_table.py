# Generated by Django 5.0 on 2023-12-24 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name': 'Product ', 'verbose_name_plural': 'Products '},
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]