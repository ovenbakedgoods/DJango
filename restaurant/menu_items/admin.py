from django.contrib import admin
from .models import Menu, Step

class StepInline(admin.StackedInline):
    model = Step

class MenuAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Step)
