# Generated by Django 3.0 on 2020-08-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='programminglanguage',
            name='bg_color',
            field=models.CharField(default='#000000', max_length=12),
        ),
    ]
