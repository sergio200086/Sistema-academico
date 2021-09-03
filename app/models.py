import abc
from django.db import models
from django.contrib.auth.models import User


class Estudiante (models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        primary_key=True,

    )
    codigo = models.IntegerField(null=False)
    def __str__(self):
        return self.usuario.email  

    class Meta:
        app_label='app'
        

    
class Profesores (models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete= models.CASCADE,
        primary_key=True,
    )
    catedra=models.BooleanField(default=False)
    def __str__(self):
         return self.usuario.last_name  
    class Meta:
        app_label='app'
    
class Grupos(models.Model):
    codigo=models.CharField(max_length=50, null=False)
    asignatura=models.CharField(max_length=50, null=False)
    semestre=models.CharField(max_length=50, null=False)
    profesor =models.ForeignKey(Profesores, related_name='grupo', null=True, on_delete=models.PROTECT)
    class Meta:
        app_label='app'

class EstudianteGrupo(models.Model):
    grupo = models.ForeignKey(Grupos, related_name = 'estudiantesgrupo', null = False, on_delete = models.PROTECT)
    estudiante = models.ForeignKey(Estudiante, related_name = 'gruposestudiante', null = False, on_delete = models.PROTECT)

    def _str_(self):
        return f'{self.estudiante.user.first_name} {self.estudiante.user.last_name} {self.grupo}'

    class Meta:
        app_label = 'app'

class Actividad(models.Model):
    descripcion = models.CharField(max_length = 100, null = False)
    grupo = models.ForeignKey(Grupos, related_name = 'actividades',null = False, on_delete = models.CASCADE)

    def _str_(self):
        return self.descripcion

    class Meta: 
        app_label = 'app'

class Nota(models.Model):
    estudiante_grupo = models.ForeignKey(EstudianteGrupo, null = False, related_name = 'notasestudiante', on_delete = models.CASCADE)
    actividad = models.ForeignKey(Actividad, related_name = 'notasactividad', null=False, on_delete = models.CASCADE)
    valor = models.FloatField(null = False,default=0)

    def _str_(self):
        return self.valor

    class Meta:
        app_label = 'app'

