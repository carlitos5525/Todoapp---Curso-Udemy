from django.shortcuts import render
from .forms import CategoryForm, TaskForm
from django.contrib import messages

# Create your views here.

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
