from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
#Importa com nome de classe a tabela do SQL
# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'html/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(username=username)

        if user:
            return HttpResponse("Já existe um usuario com esse username")

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return HttpResponse('Usuário Cadastrado com Sucesso')
     
def login(request):
    if request.method == "GET":
        return render(request, 'html/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
            return HttpResponse('válido')
        else:
            return HttpResponse('Email ou Senha Inválido')

@login_required(login_url="/auth/login/")        
def plataforma(request):
        HttpResponse("Está na plataforma")        
