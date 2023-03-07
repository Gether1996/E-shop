# Generated by Django 4.1.5 on 2023-03-01 19:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import online_store.settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('PayPal', 'PayPal'), ('Bank Transfer', 'BankTransfer'), ('Apple pay', 'ApplePay'), ('Google pay', 'GooglePay'), ('Credit card', 'CreditCard')], default=online_store.settings.PaymentMethods['CreditCard'], max_length=32)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('cart', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.cart')),
            ],
        ),
    ]
