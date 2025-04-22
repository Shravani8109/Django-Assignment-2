from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', "due_date","is_completed"]