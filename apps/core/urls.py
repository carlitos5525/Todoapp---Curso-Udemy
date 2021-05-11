from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('buscar', views.search_tasks, name='search_tasks'),
    path('', views.home, name='home'),
]
