# Generated by Django 4.1.5 on 2023-03-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_cart_bought_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='bought_items',
            field=models.TextField(),
        ),
    ]
