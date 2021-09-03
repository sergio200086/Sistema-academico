# Generated by Django 3.2 on 2021-05-11 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_alter_estudiante_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='cod',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]