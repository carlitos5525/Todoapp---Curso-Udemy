from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, TaskForm
from django.contrib import messages
from .models import Category, Task
from django.contrib.auth.decorators import login_required

@login_required(login_url='/contas/login/')
def add_category(request):
    template_name = 'task/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso')

    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_categories(request):
    template_name = 'task/list_categories.html'
    categories = Category.objects.filter(owner = request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_category(request, id_category):
    template_name = 'task/edit_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_categories')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_category(request, id_category):
    category = Category.objects.get(id = id_category)
    if category.owner == request.user:
        category.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir esta categoria.')
        return redirect('core:home')
    return redirect('tasks:list_categories')

@login_required(login_url='/contas/login/')
def add_task(request):
    template_name = 'task/add_task.html'
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Tarefa criada com sucesso.')
        else:
            print(form.erros)
    
    form = TaskForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_tasks(request):
    template_name = 'task/list_tasks.html'
    context = {}
    tasks = Task.objects.filter(owner = request.user).exclude(status = 'CD')
    context['tasks'] = tasks
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_task(request, id_task):
    template_name = 'task/edit_task.html'
    context = {}
    task = get_object_or_404(Task, id=id_task, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_tasks')
    form = TaskForm(instance=task)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_task(request, id_task):
    task = get_object_or_404(Task, id=id_task)
    if task.owner == request.user:
        task.delete()
        return redirect('task:list_tasks')
    else:
        messages.error('Você não tem permissão para excluir essa tarefa')
        return redirect('core:home')