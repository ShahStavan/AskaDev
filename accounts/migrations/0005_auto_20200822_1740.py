# Generated by Django 3.0 on 2020-08-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(help_text='A Short Bio about yourself', max_length=200),
        ),
    ]
