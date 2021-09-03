from django.urls import path

from . import views

app_name = 'app' 
urlpatterns=[
    path('index/', views.index, name='index'),
    path('index/perfil/', views.iniciar_sesion, name='iniciar_sesion'),
    # path('index/estudiante/', views.estudiante, name='estudiante'),
    # path('index/estudiante/', views.estudiante, name='estudiante'), 
    # verGrupoEstudiante
    # path('index/estudiante/verGrupoEstudiante/<int:id>/', views.verGrupoEstudiante, name='verGrupoEstudiante'),
    path('index/estudiante/verGrupoEstudiante/<int:idgrupo>/<int:idestudiante>/', views.verGrupoEstudiante, name='verGrupoEstudiante'),
    path('logout/', views.cerrarsesion, name='cerrarsesion'),

    path('index/profesor/crearAcividadProfesor/<int:id>/', views.crearAcividadProfesor, name='crearAcividadProfesor'),
    # path('index/profesor/', views.crearActividadProfesorForm, name='crearActividadProfesorForm'),
    path('index/profesor/editaractividadForm/<int:id>/', views.editaractividadForm, name='editaractividadForm'),
    path('index/profesor/editaractividad/<int:id>/', views.editaractividad, name='editaractividad'),
    path('index/profesor/crearActividadProfesorForm/', views.crearActividadProfesorForm, name='crearActividadProfesorForm'),
    path('index/profesor/verGrupoProfesor/<int:id>/', views.verGrupoProfesor, name='verGrupoProfesor'),
    path('index/profesor/verActividadProfesor/<int:idactividad>/<int:idgrupo>/', views.verActividadProfesor, name='verActividadProfesor'),
    path('index/profesor/verEstudianteComoProfesor/<int:idestudiante>/<int:idgrupo>/', views.verEstudianteComoProfesor, name='verEstudianteComoProfesor'),
    path('index/profesor/cambiarnota/<int:idgrupoestudiante>/<int:idactividad>/', views.cambiarnota, name='cambiarnota'),
    path('index/admin/', views.admin, name='admin'), 
    path('index/admin/verListaEstudiantes', views.verListaEstudiantes, name='verListaEstudiantes'),
    path('index/admin/eliminargrupo/<int:id>/', views.eliminargrupo, name='eliminargrupo'),
    path('index/admin/editarEstudiante/<int:id>/', views.editarEstudiante, name='editarEstudiante'),
    path('index/admin/editarestudianteForm/<int:id>/', views.editarestudianteForm, name='editarestudianteForm'),
    path('index/admin/verGruposComoAdmin', views.verGruposComoAdmin, name='verGruposComoAdmin'),
    path('index/admin/verGrupoindividualAdmin/<int:id>/', views.verGrupoindividualAdmin, name='verGrupoindividualAdmin'), #REVISAR
    path('index/admin/editarGrupoAdmin/<int:id>/', views.editarGrupoAdmin, name='editarGrupoAdmin'),
    path('index/admin/editarGrupoAdminForm/<int:id>/', views.editarGrupoAdminForm, name='editarGrupoAdminForm'),
    path('index/admin/agregarEstudianteAGrupo/<int:id>/', views.agregarEstudianteAGrupo, name='agregarEstudianteAGrupo'),
    path('index/admin/agregarestudianteagrupoForm/<int:idestudiante>/<int:idgrupo>', views.agregarestudianteagrupoForm, name='agregarestudianteagrupoForm'),
    path('index/admin/verProfesores', views.verProfesores, name='verProfesores'),
    path('index/admin/crearGrupoAdmin', views.crearGrupoAdmin, name='crearGrupoAdmin'),
    path('index/admin/crearProfesor', views.crearProfesor, name='crearProfesor'),
    path('index/admin/crearProfesorForm', views.crearProfesorForm, name='crearProfesorForm'),
    path('index/admin/crearEstudiante', views.crearEstudiante, name='crearEstudiante'),
    path('index/admin/crearEstudianteForm', views.crearEstudianteForm, name='crearEstudianteForm'),
    path('index/admin/crearGrupoForm', views.crearGrupoForm, name='crearGrupoForm'),
    path('index/error',views.error, name = 'error'),
    path('index/completado',views.completado, name = 'completado'),
    path('index/admin/listaDeCursosProfe/<int:id>',views.listaDeCursosProfe, name = 'listaDeCursosProfe'),
    

]
