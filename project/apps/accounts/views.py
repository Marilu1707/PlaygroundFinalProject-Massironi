from django.shortcuts import render

def index(request):
    context = {"app_name": "Spiderweb"}
    return render(request, "core/index.html",context)

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import UserExtension
from accounts.forms import FormularioRegistro, FormularioEditarPerfil, FormularioChangePassword

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        formulario_login = AuthenticationForm(request, data=request.POST)
        if formulario_login.is_valid():
            user = formulario_login.get_user()
            login(request, user)
            UserExtension.objects.get_or_create(user=request.user)
            return redirect('home')
    else:
        formulario_login = AuthenticationForm()

    return render(request, 'accounts/login.html', { 'formulario_login' : formulario_login })

def registrar_cuenta(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        formulario_registro = FormularioRegistro(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect('home')
    else:
        formulario_registro = FormularioRegistro()

    return render(request, 'accounts/registrar.html', { 'formulario_registro' : formulario_registro })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required
def ver_perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario_editar_perfil = FormularioEditarPerfil(request.POST, request.FILES)

        if formulario_editar_perfil.is_valid():
            datos_perfil = formulario_editar_perfil.cleaned_data

            user = request.user
            user.email = datos_perfil['email']
            user.first_name = datos_perfil['first_name']
            user.last_name = datos_perfil['last_name']

            if not datos_perfil['avatar']:
                user.userextension.avatar = None
            elif datos_perfil['avatar']:
                user.userextension.avatar = datos_perfil['avatar']

            user.userextension.descripcion = datos_perfil['descripcion']
            user.userextension.link = datos_perfil['link']

            user.save()
            user.userextension.save()

            return redirect('ver_perfil')
    else:
        formulario_editar_perfil = FormularioEditarPerfil(
            initial={
                'email' : request.user.email,
                'first_name' : request.user.first_name,
                'last_name' : request.user.last_name,
                'avatar' : request.user.userextension.avatar,
                'descripcion' : request.user.userextension.descripcion,
                'link' : request.user.userextension.link,
            }
        )

    return render(request, 'accounts/editar_perfil.html', { 'formulario_editar_perfil' : formulario_editar_perfil })

@login_required
def cambiar_password(request):
    if request.method == 'POST':
        formulario_cambio_password = FormularioChangePassword(user=request.user, data=request.POST)

        if formulario_cambio_password.is_valid():
            formulario_cambio_password.save()
            update_session_auth_hash(request, request.user)
            return redirect('ver_perfil')
    else:
        formulario_cambio_password = FormularioChangePassword(user=request.user)

    return render(request, 'accounts/change_password.html', { 'formulario_cambio_password' : formulario_cambio_password })
