from django.contrib import admin
from .models import Category, Task
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'end_date', 'priority']

admin.site.register(Category, CategoryAdmin)
