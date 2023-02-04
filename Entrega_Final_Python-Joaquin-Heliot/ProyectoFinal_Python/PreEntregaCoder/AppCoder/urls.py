from django.urls import path
from django.views.generic.base import TemplateView
from AppCoder import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('productos', views.productos, name="Productos"),
    path('sobreMi', views.sobreMi, name="sobreMi"),
    path('clientes', views.clientes, name="Clientes"),
    path('cursos', views.cursos, name="Cursos"),
    path('consultasFormulario', views.consultasFormulario, name="consultasFormulario"),
    path('busquedaCurso', views.busquedaCurso, name="busquedaCurso"),
    path('buscar/', views.buscar),
    
    path('producto/list', views.ProductoList.as_view(), name='List'),
    
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detail'),
    
    path(r'^nuevo$', views.ProductoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete'),
  
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
]
