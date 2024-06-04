from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import formulario
from .views import lista_clientes

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.login, name='login'),
    path('formulario/', views.formulario, name='formulario'),
    path('success/', TemplateView.as_view(template_name='html/success.html'), name='success'),  # Página de sucesso
     path('lista_clientes/', lista_clientes, name='lista_clientes')
]