from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('adicionar', views.add_category, name='add_category'),
    path('', views.list_categories, name='list_categories')
]