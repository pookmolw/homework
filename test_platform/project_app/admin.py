from django.contrib import admin
from project_app.models import Project
# Register your models here.

"""
from . import models

admin.site.register(models.Article)
"""

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name','describe','status','create_time','update_time']
	list_filter = ['status']
	search_fields = ['name']

admin.site.register(Project,ProjectAdmin)