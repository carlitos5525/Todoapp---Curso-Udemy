from django.contrib import admin
from .models import Category, Task
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task)