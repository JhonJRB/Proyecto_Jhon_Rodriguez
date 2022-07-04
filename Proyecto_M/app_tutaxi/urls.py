from django.urls import path
from app_tutaxi import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name='inicio' ),
    #*********************Cargar datos*******************************
    path('cargarcliente/',views.cargar_cliente, name='cargar_cliente' ),
    path('cargarmovil/',views.cargar_movil, name='cargar_movil' ),
    path('cargarchofer/',views.cargar_chofer, name='cargar_chofer' ),
    #*********************Ver datos***********************************
    path('verchofer/',views.ver_chofer, name='ver_chofer' ),
    path('vermovil/',views.ver_movil, name='ver_movil' ),
    path('vercliente/',views.ver_cliente, name='ver_cliente' ),
    #*********************Buscar datos*******************************
    path('buscarchofer/',views.buscar_chofer, name='buscar_chofer' ),
    path('traerchofer/',views.traer_chofer, name='traer_chofer' ),
    path('buscarmovil/',views.buscar_movil, name='buscar_movil' ),
    path('traermovil/',views.traer_movil, name='traer_movil' ),
    path('buscarcliente/',views.buscar_cliente, name='buscar_cliente' ),
    path('traercliente/',views.traer_cliente, name='traer_cliente' ),
    #*********************Eliminar datos*******************************
    path('eliminarchofer/<int:id>',views.eliminar_chofer, name='eliminar_chofer'),
    path('eliminarmovil/<int:id>',views.eliminar_movil, name='eliminar_movil'),
    path('eliminarcliente/<int:id>',views.eliminar_cliente, name='eliminar_cliente'),
    #*********************Editar datos*******************************
    path('editarchofer/<int:id>',views.editar_chofer, name='editar_chofer'),
    path('editarmovil/<int:id>',views.editar_movil, name='editar_movil'),
    path('editarcliente/<int:id>',views.editar_cliente, name='editar_cliente'),
    #*********************User Registro*******************************
    path('login_r',views.login_r, name='login_r'),
    path('registro',views.registro, name='registro'),
    path('logout',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_perfil',views.editar_perfil, name='editar_perfil'),
    #**********************Aboutme***************************************
    path('aboutme',views.aboutme, name='aboutme')
    #path('agregaravatar', views.agregar_avatar, name='agregar_avatar')
  ]