# Generated by Django 4.2.7 on 2023-11-13 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='booking',
            table='Booking',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='Menu',
        ),
    ]
