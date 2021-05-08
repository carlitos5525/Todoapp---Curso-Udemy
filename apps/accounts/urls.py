from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('novo_usuario/', views.add_user, name='add-user'),
    path('login/', views.user_login, name='login'),
    path('sair/', views.user_logout, name='logout'),
    path('alterar_senha/', views.user_change_password, name='alterar_senha'),
    path('novo_perfil/', views.add_user_profile, name='add_user_profile'),
    path('perfil/', views.list_user_profile, name='list_user_profile'),
    path('editar_perfil/<slug:username>', views.change_user_profile, name='change_user_profile'),
    path('editar_usuario/<slug:username>', views.change_user_information, name='change_user_information',)
]
