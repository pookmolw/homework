from django.contrib import admin
from module_app.models import Module

class ModuleAdmin(admin.ModelAdmin):
	list_display = ['project','name','describe','create_time','update_time']

admin.site.register(Module,ModuleAdmin)