# Generated by Django 2.2.6 on 2020-08-24 12:13

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('questions', '0004_auto_20200824_1742'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tags',
            table='Tags',
        ),
    ]
