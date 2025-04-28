from django.contrib import admin
from .models import Professor, Module, ModuleInstance, Rating

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

@admin.register(ModuleInstance)
class ModuleInstanceAdmin(admin.ModelAdmin):
    list_display = ('module', 'year', 'semester')
    list_filter = ('year', 'semester')
    filter_horizontal = ('professors',)
    search_fields = ('module__code', 'module__name')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'professor', 'module_instance', 'rating')
    list_filter = ('rating',)
    search_fields = ('professor__name', 'module_instance__module__name', 'user__username')
