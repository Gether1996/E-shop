# Generated by Django 4.1.5 on 2023-03-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='payed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]