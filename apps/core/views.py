from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from task.models import Task
from datetime import datetime
# Create your views here.

@login_required(login_url='/contas/login/')
def home(request):
    template_name = 'core/core.html'
    context = {}
    today_tasks = Task.objects.filter(owner=request.user, end_date=datetime.today()).exclude(status='CD')
    context['tasks'] = today_tasks
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
def search_tasks(request):
    template_name = 'task/list_tasks.html'
    context = {}
    tasks = Task.objects.filter(owner=request.user)
    if request.GET.get('query'):
        query = request.GET.get('query')
        tasks = tasks.filter(name__icontains=query)
    if request.GET.get('is_conclued'):
        if request.GET.get('is_conclued') == 'on':
            print('here')
            tasks = tasks.filter(status='CD')
    if request.GET.get('date_start_with') and request.GET.get('date_end_with'):
        start_with = request.GET.get('date_start_with') 
        end_with = request.GET.get('date_end_with')
        tasks = tasks.filter(end_date__range=(start_with, end_with))
    context['tasks'] = tasks
    return render(request, template_name, context)