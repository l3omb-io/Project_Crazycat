# Generated by Django 4.0.2 on 2022-02-09 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_basket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.basket'),
        ),
    ]