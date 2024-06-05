from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cliente, Processo, Atualizacao
from django.http import HttpResponseRedirect
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
    clientes = Cliente.objects.all().prefetch_related('processo_set__atualizacao_set')
    return render(request, 'html/lista_clientes.html', {'clientes': clientes})

def editar_cliente(request, cliente_id):
    # Obtenha a instância do cliente que está sendo editado
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        # Preencha o formulário com os dados do cliente e os dados POST
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            # Salve as alterações no cliente
            form.save()
            # Redirecione para a página de lista de clientes após a edição
            return redirect('lista_clientes')
    else:
        # Se a solicitação não for POST, exiba o formulário preenchido com os dados do cliente
        form = ClienteForm(instance=cliente)

    # Renderize o template de edição do cliente com o formulário
    return render(request, 'editar_cliente.html', {'form': form})

def excluir_cliente(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('id')
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.delete()
        return redirect('lista_clientes')

def adicionar_atualizacao(request):
    if request.method == 'POST':
        processo_id = request.POST.get('processo_id')
        processo = get_object_or_404(Processo, id=processo_id)
        form = AtualizacaoForm(request.POST)
        if form.is_valid():
            atualizacao = form.save(commit=False)
            atualizacao.processo = processo
            atualizacao.save()
            return redirect('lista_clientes')