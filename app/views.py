from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import   Estudiante, EstudianteGrupo, Profesores, Grupos, Actividad, Nota
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'app/index.html')
@login_required
def editarEstudiante(request,id):
    estudianteenviado=Estudiante.objects.get(usuario_id=id)
    contexto= {
        'estudianteenviado':estudianteenviado
    }
    return render( request, 'app/editarEstudiante.html',contexto)
@login_required
def editarestudianteForm(request,id):
    editarestudiante=Estudiante.objects.get(usuario_id=id)

    editarestudiante.codigo=request.POST['codigo']
    editarestudiante.usuario.last_name=request.POST['apellidos']
    editarestudiante.usuario.first_name=request.POST['nombre']
    editarestudiante.usuario.email=request.POST['correo']
    # ARREGLAR REPETICIÖN ESTUDIANTE----------------------------
    if editarestudiante.codigo=="" or editarestudiante.usuario.last_name==""  or editarestudiante.usuario.first_name=="" or editarestudiante.usuario.email=="":
        contexto = {
            'erroreditargrupo': 'Ningún campo puede quedar vacio'
        }
        return render(request,'app/error.html',contexto)
    else:
        editarestudiante.usuario.save()

    return redirect('app:verListaEstudiantes')

@login_required
def verGruposComoAdmin(request):
    vergrupos=Grupos.objects.all()
    contexto={
        'grupos':vergrupos
    }

    return render(request, 'app/verGruposComoAdmin.html',contexto)
@login_required
def verGrupoEstudiante(request,idgrupo,idestudiante):
    estudiantegrupo=EstudianteGrupo.objects.get(estudiante_id=idestudiante,grupo_id=idgrupo)
    print(estudiantegrupo)
    contexto = {
        'estudiantegrupo':estudiantegrupo
        }
    return render(request,'app/verGrupoEstudiante.html',contexto)
@login_required
def verEstudianteComoProfesor(request, idestudiante,idgrupo):
    estudianteEnviado=Estudiante.objects.get(usuario_id=idestudiante)
    grupollegada=Grupos.objects.get(id=idgrupo)
    estudiantegrupollegada=EstudianteGrupo.objects.get(estudiante_id=idestudiante,grupo_id=idgrupo)
    print(estudiantegrupollegada)
    contexto={
        'estudianteEnviado':estudianteEnviado,
        'grupollegada':grupollegada,
        'estudiantegrupollegada':estudiantegrupollegada

    }
    
    return render(request, 'app/verEstudianteComoProfesor.html', contexto)
@login_required
def verActividadProfesor(request, idactividad,idgrupo):
    actividadllegada=Actividad.objects.get(id=idactividad)
    grupollegada=Grupos.objects.get(id=idgrupo)
    miactividad=actividadllegada.id
    notallegada=Nota.objects.filter(actividad_id=miactividad)
    contexto={
        'actividadllegada': actividadllegada,
        'grupollegada':grupollegada,
        'notallegada':notallegada
    }
    return render(request, 'app/verActividadProfesor.html', contexto)
@login_required
def verListaEstudiantes(request):

    lista_verEstudiantes=Estudiante.objects.all().order_by('codigo')
    contexto={
        'estudiantes':lista_verEstudiantes
    }
    
    return render (request,'app/verListaEstudiantes.html',contexto)
@login_required
def crearAcividadProfesor(request,id):
    lista= Profesores.objects.get(usuario_id=id)
    grupos=Grupos.objects.filter(profesor=id)
    contexto = {
        'profesor': lista,
        'grupos':grupos
    }
    return render(request, 'app/crearAcividadProfesor.html', contexto)
@login_required
def editaractividad(request,id):
    actividadactual=Actividad.objects.get(id=id)
    contexto={
    'actividadactual':actividadactual
    }

    return render(request,'app/editaractividad.html' ,contexto)
@login_required
def editaractividadForm(request,id):
    cambiodescripcion=Actividad.objects.get(id=id)
    cambiodescripcion.descripcion=request.POST['descripcion']
    if cambiodescripcion=="":
        contexto = {
            'errorcreacionestudiante': 'Los campos marcados con * deben ser llenados obligatoriamente'
        }
        return render(request,'app/error.html',contexto)

    cambiodescripcion.save()
    return redirect('app:completado')
@login_required
def cambiarnota(request,idgrupoestudiante,idactividad):
    notaenviada=request.POST['nota']
    if notaenviada=="":
        contexto = {
            'errorcreacionestudiante': 'La nota no puede estar vacía ni menor a 0 o mayor a 5'
        }
        return render(request,'app/error.html',contexto)

    
    notanueva=Nota()
    notanueva.valor=notaenviada
    act=Actividad.objects.get(id=idactividad)
    notanueva.actividad=act
    e_g=EstudianteGrupo.objects.get(id=idgrupoestudiante)
    notanueva.estudiante_grupo=e_g
    for checknotas in Nota.objects.all():
        if checknotas.actividad==act and checknotas.estudiante_grupo==e_g:
            print(checknotas)
            checknotas.valor=notaenviada
            checknotas.save()
            return redirect('app:completado')
    notanueva.save()
    return redirect('app:completado')
    
@login_required
def crearActividadProfesorForm(request):
    nuevaactividad=Actividad()
    nuevaactividad.descripcion=request.POST['descripcion']
    grupollegada=request.POST['grupo']
    g=Grupos.objects.get(pk=grupollegada)
    nuevaactividad.grupo=g
    if nuevaactividad.grupo=="" or nuevaactividad.descripcion=="":
        contexto = {
            'errorcreacionestudiante': 'Los campos marcados con * deben ser llenados obligatoriamente'
        }
        return render(request,'app/error.html',contexto)
    nuevaactividad.save()
    return redirect('app:completado')

@login_required    
def admin(request):
    return render(request,'app/admin.html')

@login_required
def verGrupoProfesor(request, id):
    grupollegada=Grupos.objects.get(id=id)
    contexto={
        'grupollegada':grupollegada
    }
    return render(request, 'app/verGrupoProfesor.html',contexto)

@login_required
def verGrupoindividualAdmin(request,id):
    grupoenviado=Grupos.objects.get(id=id)
    contexto ={
        'grupoenviado':grupoenviado   
    }
    return render(request, 'app/verGrupoindividualAdmin.html',contexto)
@login_required
def editarGrupoAdmin(request,id):
    grupoenviado=Grupos.objects.get(id=id)
    profesoresaenviar=Profesores.objects.all()
    contexto= {
        'grupoenviado':grupoenviado,
        'profesoresaenviar':profesoresaenviar
    }

    return render(request, 'app/editarGrupoAdmin.html',contexto)
@login_required    
def editarGrupoAdminForm(request,id):
    grupo=Grupos.objects.get(id=id)
    grupo.codigo=request.POST['codigo']
    grupo.asignatura=request.POST['asignatura']
    profesor=request.POST['profesor']
    p=Profesores.objects.get(pk=profesor)
    grupo.profesor=p
    grupo.semestre=request.POST['semestre']
    if grupo.codigo=="" or grupo.asignatura==""  or grupo.semestre=="":
        contexto = {
            'erroreditargrupo': 'Ningún campo puede quedar vacio'
        }
        return render(request,'app/error.html',contexto)
    else:
        grupo.save()
        return redirect('app:verGruposComoAdmin')


@login_required    
def agregarEstudianteAGrupo(request,id):
    grupoenviado=Grupos.objects.get(id=id)
    estudiantes=Estudiante.objects.all()
    
    contexto={
        'grupoenviado':grupoenviado,
        'estudiantes':estudiantes
    }

    return render(request,'app/agregarEstudianteAGrupo.html',contexto)
@login_required
def verProfesores(request):
    #obtiene profesores
    lista_verProfesores=Profesores.objects.all().order_by('usuario_id')
    contexto={
        'profesores':lista_verProfesores
    }
    
    return render(request, 'app/verProfesores.html', contexto)
@login_required
def crearGrupoAdmin(request):
    lista=Profesores.objects.all()
    contexto={
        'profesores':lista
    }
    return render(request, 'app/crearGrupoAdmin.html',contexto)
@login_required
def crearProfesor(request):
    return render(request, 'app/crearProfesor.html')
@login_required
def crearEstudiante(request):

    return render(request, 'app/crearEstudiante.html')
@login_required
def listaDeCursosProfe(request, id):
    lista= Profesores.objects.get(usuario_id=id)
    grupos=Grupos.objects.filter(profesor=id).order_by('semestre')
    contexto = {
        'profesor': lista,
        'grupos':grupos
    }
    return render(request, 'app/listaDeCursosProfe.html', contexto)
@login_required
def error(request):
    return render(request,'app/error.html')
@login_required
def completado(request):
    return render(request,'app/completado.html')


@login_required
def crearProfesorForm(request):
    apellidosProfe = request.POST['apellidosProfe']
    nombreProfe = request.POST['nombresProfe']
    emailProfe = request.POST['emailProfe']
    contraProfe = request.POST['contraProfe']
    catedra = request.POST['catedra']
    if apellidosProfe=="" or nombreProfe=="" or emailProfe =="" or contraProfe=="":
        
        return redirect('app:error')
    else:
        for estudiantescreados in User.objects.all():
            if estudiantescreados.email == emailProfe:
                contexto = {'repetircorreo': 'No se puede repetir correo'             }
                return render(request,'app/error.html',contexto)
        
        us = User.objects.create_user(username=emailProfe, first_name=nombreProfe, last_name=apellidosProfe, email=emailProfe, password=contraProfe )
        us.save()
        profe = Profesores(usuario=us, catedra=catedra)
        profe.save()
        return redirect('app:verProfesores')
@login_required
def crearEstudianteForm(request):
    apellidosEst=request.POST['apellidosEst']
    nombreEst=request.POST['nombresEst']
    codigoEst=request.POST['codigoEst']
    emailEst=request.POST['emailEst']
    contraEst=request.POST['contraEst']
    
    if apellidosEst=="" or nombreEst=="" or codigoEst=="" or emailEst=="" or contraEst=="":
        contexto = {
            'errorcreacionestudiante': 'Los campos marcados con * deben ser llenados obligatoriamente'
        }
        return render(request,'app/error.html',contexto)
    else:
        for estudiantescreados in User.objects.all():
            if estudiantescreados.email == emailEst:
                contexto = {'repetircorreo': 'No se puede repetir correo'             }
                return render(request,'app/error.html',contexto)

        nuevoest=User.objects.create_user(username=emailEst, first_name=nombreEst, last_name=apellidosEst, email=emailEst, password=contraEst)
        nuevoest.save()
        estudiante=Estudiante(usuario=nuevoest, codigo=codigoEst)
        estudiante.save()
        return redirect('app:verListaEstudiantes')
@login_required
def crearGrupoForm(request):
    codgrupo=request.POST['codgrupo']
    asignatura=request.POST['asignatura']
    id_profesor=int(request.POST['profesor'])
    semestre=request.POST['semestre']
    profesor=Profesores.objects.get(pk=id_profesor)

    if codgrupo=="" or asignatura=="" or semestre=="":
        contexto = {
            'erroreditargrupo': 'Ningún campo puede quedar vacio'
        }
        return render(request,'app/error.html',contexto)
    else:
        nuevogrupo=Grupos(codigo=codgrupo, asignatura=asignatura, semestre=semestre, profesor=profesor)
        nuevogrupo.save()
        return redirect('app:verGruposComoAdmin')        

def iniciar_sesion(request):
    # Obtiene los datos digitados por el usuario
    u = request.POST['USUARIO']
    p = request.POST['password']
    usuario = authenticate(username=u, password=p)
    # Verifica que el usuario sea válido
    if usuario is not None:
        if usuario.is_superuser==True:
            login(request, usuario)
            return redirect('app:admin')
        for varprofesores in Profesores.objects.all():
            if varprofesores.usuario.username ==u:
                print("log as Teacher")
                login(request, usuario)

                grupos=Grupos.objects.filter(profesor=varprofesores.usuario.id)
                print(grupos)
                contexto={
                    'varprofesores':varprofesores,
                    'grupos':grupos
                }
                return render(request,'app/profesor.html', contexto)
        for varestudiantes in Estudiante.objects.all():
            if varestudiantes.usuario.username==u:
                login(request, usuario)
                print(varestudiantes)
                idestudiante=varestudiantes.usuario.id
                grupos=EstudianteGrupo.objects.filter(estudiante=idestudiante)
                print(grupos)
                contexto={
                    'varestudiantes':varestudiantes,
                    'grupos':grupos
                }
                return render(request,'app/estudiante.html',contexto)
        
    
    else:
        contexto = {
            'errorlogin': 'Credenciales no válidas'
        }
        return render(request,'app/error.html',contexto)
@login_required
def eliminargrupo(request,id):
    grupo=Grupos.objects.get(id=id)
    grupo.delete()

    return redirect('app:verGruposComoAdmin')
@login_required
def agregarestudianteagrupoForm(request,idestudiante,idgrupo):
    grupo=Grupos.objects.get(id=idgrupo)
    estudiantellegada=Estudiante.objects.get(usuario_id=idestudiante)
    check=EstudianteGrupo.objects.filter(grupo=idgrupo)

    for est in check:
        if est.estudiante==estudiantellegada:
            contexto = {
            'errorrepetirestudiante': 'El estudiante ya está en el grupo'
            }
            return render(request,'app/error.html',contexto)
            
    nuevarelacion=EstudianteGrupo()
    nuevarelacion.grupo=grupo
    nuevarelacion.estudiante=estudiantellegada
    nuevarelacion.save()

    return redirect('app:verGruposComoAdmin')
@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('app:index')