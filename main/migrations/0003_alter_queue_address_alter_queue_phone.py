# Generated by Django 5.1.4 on 2025-01-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_queue_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='address',
            field=models.CharField(choices=[('Address1', 'Manzil 1'), ('Address2', 'Manzil 2')], max_length=20),
        ),
        migrations.AlterField(
            model_name='queue',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
