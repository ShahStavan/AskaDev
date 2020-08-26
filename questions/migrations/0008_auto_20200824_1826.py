# Generated by Django 2.2.6 on 2020-08-24 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asked_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='Django Question', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='questions.Tags'),
        ),
    ]
