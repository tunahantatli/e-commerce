# Generated by Django 4.2.1 on 2023-05-20 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='qantity',
            new_name='quantity',
        ),
    ]
