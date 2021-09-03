# Generated by Django 3.2 on 2021-06-13 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210518_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='app.grupos')),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gruposestudiante', to='app.estudiante')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estudiantesgrupo', to='app.grupos')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notasactividad', to='app.actividad')),
                ('estudiante_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notasestudiante', to='app.estudiantegrupo')),
            ],
        ),
    ]
