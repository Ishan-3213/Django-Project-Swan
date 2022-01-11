# Generated by Django 4.0.1 on 2022-01-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_productimage_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
