from django.contrib import admin

from .models import tasks


class tasksAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
admin.site.register(tasks,tasksAdmin)
