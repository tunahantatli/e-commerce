# Generated by Django 4.2.1 on 2023-05-16 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='zip_code',
            new_name='zipcode',
        ),
    ]
