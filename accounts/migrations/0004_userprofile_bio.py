# Generated by Django 3.0 on 2020-08-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200822_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]