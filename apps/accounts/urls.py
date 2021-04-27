from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('novo_usuario/', views.add_user, name='add-user'),
]