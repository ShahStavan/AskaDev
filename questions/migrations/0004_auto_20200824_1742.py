# Generated by Django 2.2.6 on 2020-08-24 12:12

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('questions', '0003_auto_20200824_1742'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tags',
            table='tags',
        ),
    ]