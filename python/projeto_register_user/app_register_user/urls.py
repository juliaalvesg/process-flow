from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import formulario
from .views import lista_clientes, editar_cliente, excluir_cliente, adicionar_atualizacao

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.login, name='login'),
    path('formulario/', views.formulario, name='formulario'),
    path('success/', TemplateView.as_view(template_name='html/success.html'), name='success'),  # Página de sucesso
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir_cliente/', views.excluir_cliente, name='excluir_cliente'),
    path('adicionar_atualizacao/', views.adicionar_atualizacao, name='adicionar_atualizacao'),
    path('register/', views.register, name='register')
]