# Generated by Django 5.0.6 on 2024-08-22 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_stock_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='sell_value',
            new_name='sale_value',
        ),
    ]
