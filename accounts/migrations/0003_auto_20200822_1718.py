# Generated by Django 3.0 on 2020-08-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200821_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(max_length=255, upload_to='static/images/profile_picture'),
        ),
    ]