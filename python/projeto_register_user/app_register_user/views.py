from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cliente
# views.py
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProcessoForm, AtualizacaoForm

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

        if User.objects.filter(username=username).exists():
            return HttpResponse("Já existe um usuário com este username.")

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return render(request, 'html/process.html')




def login(request):
    if request.method == "GET":
        return render(request, 'html/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticando usando o nome de usuário
        user = authenticate(request, username=username, password=password)
        
        if user:
            # Efetuando o login
            login_django(request, user)
            return HttpResponse('Login válido')
        else:
            return HttpResponse('Nome de usuário ou senha inválidos')


@login_required(login_url="/auth/login/")        
def plataforma(request):
        HttpResponse("Está na plataforma")        

def formulario(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        processo_form = ProcessoForm(request.POST)
        atualizacao_form = AtualizacaoForm(request.POST)
        
        if cliente_form.is_valid() and processo_form.is_valid() and atualizacao_form.is_valid():
            cliente = cliente_form.save()
            processo = processo_form.save(commit=False)
            processo.cliente = cliente
            processo.save()
            atualizacao = atualizacao_form.save(commit=False)
            atualizacao.processo = processo
            atualizacao.save()
            return redirect('success')  # Redirecione para uma página de sucesso
    else:
        cliente_form = ClienteForm()
        processo_form = ProcessoForm()
        atualizacao_form = AtualizacaoForm()

    return render(request, 'html/formulario.html', {
        'cliente_form': cliente_form,
        'processo_form': processo_form,
        'atualizacao_form': atualizacao_form
    })

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'html/lista_clientes.html', {'clientes': clientes})