# Generated by Django 4.0.1 on 2022-01-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='purchased',
            field=models.BooleanField(default=0),
        ),
    ]