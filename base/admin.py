from django.contrib import admin
from .models import (
    dakhl
)


@admin.register(dakhl)
class CourseAdmin(admin.ModelAdmin):
    list_display=['user']
    
