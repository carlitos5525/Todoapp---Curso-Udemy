from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, "Usuário salvo com sucesso.")
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


def user_login(request):
    template_name = 'accounts/user_login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, template_name, {})


@login_required(login_url='/contas/login/')
def user_logout(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='contas/login/')
def user_change_password(request):
    template_name = 'accounts/user_change_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Senha alterada com sucesso.')
        else:
            messages.error(request, "Não foi possível trocar a senha.")
            messages.error(request, form.errors)
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)