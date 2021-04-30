from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('novo_usuario/', views.add_user, name='add-user'),
    path('login/', views.user_login, name='login'),
    path('sair/', views.user_logout, name='logout'),
    path('alterar_senha/', views.user_change_password, name='alterar_senha'),
    path('perfil/', views.add_user_profile, name='add_user_profile'),
]