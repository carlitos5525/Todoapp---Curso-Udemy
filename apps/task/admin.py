from django.contrib import admin
from .models import Category, Task
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['owner']


def mark_all_tasks_done(modeladmin, request, queryset):
    queryset.update(status='CD')
mark_all_tasks_done.short_description = "Marcar tarefas como concluídas"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'end_date', 'priority', 'status', 'list_categories']
    search_fields = ['name', 'end_date']
    list_filter = ['category']
    actions = [mark_all_tasks_done]

    def list_categories(self, obj):
        return ", ".join([c.name for c in obj.category.all()])
    list_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
