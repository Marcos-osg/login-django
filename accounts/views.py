from django.contrib import auth, messages
from django.shortcuts import redirect, render
from accounts.models import User
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuario ou senha invalidos')
        return render(request,'accounts/login.html')
    else:
        auth.login(request,user)
        messages.success(request,'Logado com sucesso')
        return redirect('sucess_login')

@login_required(redirect_field_name='login')
def loginsucess(request):
    return render(request, 'accounts/login_sucess.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastrar(request):
    if request.method != 'POST':
        return render(request,'accounts/cadastrar.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode estar vazio')
        return render(request,'accounts/cadastrar.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'Email invalido')
        return render(request,'accounts/cadastrar.html')
    if senha != senha2:
        messages.error(request,'Senhas não conferem')
        return render(request,'accounts/cadastrar.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request,'Usuário já cadastrado')
        return render(request,'accounts/cadastrar.html')
    if User.objects.filter(email=email).exists():
        messages.error(request,'Email já cadastrado')
        return render(request,'accounts/cadastrar.html')
    messages.success(request,'Cadastrado com sucesso! Efetue o login')

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    
    return redirect('login')


def index(request):
    return render (request, 'accounts/index.html')