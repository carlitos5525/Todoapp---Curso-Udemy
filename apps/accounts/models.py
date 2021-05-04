from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    photo = models.ImageField(verbose_name='Foto', upload_to='photos')
    cell_phone = models.CharField(verbose_name='Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfis do Usuário'

    def __str__(self):
        return self.user.username
