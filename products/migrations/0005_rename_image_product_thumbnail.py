# Generated by Django 4.2.3 on 2023-10-21 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='thumbnail',
        ),
    ]
