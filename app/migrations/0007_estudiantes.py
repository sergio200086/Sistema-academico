# Generated by Django 3.2 on 2021-05-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210508_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(default='', max_length=100)),
                ('nombres', models.CharField(default='', max_length=100)),
                ('contraseña', models.CharField(default='', max_length=100)),
                ('correo', models.EmailField(default='', max_length=100)),
                ('codigo', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
