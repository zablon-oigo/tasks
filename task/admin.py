from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['title','body','status','created_by','updated_at']
    list_filter=['created_at','updated_at']
    list_editable=['status']
    prepopulated_fields={'slug':('title',)}
