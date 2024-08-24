# Generated by Django 5.0.6 on 2024-08-20 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
        ('peoples', '0004_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='amount',
            new_name='paid_amount',
        ),
        migrations.CreateModel(
            name='CustomerDueReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_due', models.IntegerField(default=0)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='peoples.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.owner')),
            ],
        ),
    ]