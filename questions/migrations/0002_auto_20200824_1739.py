# Generated by Django 2.2.6 on 2020-08-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questions.Tags'),
            preserve_default=False,
        ),
    ]
