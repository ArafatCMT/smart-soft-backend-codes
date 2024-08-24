# Generated by Django 5.0.6 on 2024-08-20 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
        ('peoples', '0005_rename_amount_salary_paid_amount_customerduereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierDueReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_due', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.owner')),
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='peoples.supplier')),
            ],
        ),
    ]