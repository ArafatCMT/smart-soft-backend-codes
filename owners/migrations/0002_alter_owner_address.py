# Generated by Django 5.0.6 on 2024-08-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
