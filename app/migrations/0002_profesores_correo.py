# Generated by Django 3.2 on 2021-05-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores',
            name='correo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]