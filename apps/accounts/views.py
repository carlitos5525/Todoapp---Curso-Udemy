from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm


def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)
