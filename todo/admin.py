from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)

admin.site.register(Todo, TodoAdmin)

# Register your models here.
