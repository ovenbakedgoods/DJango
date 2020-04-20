from django.contrib import admin
from .models import Coldbean, Step
class StepInline(admin.StackedInline):
    model = Step

class ColdbeanAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Coldbean, ColdbeanAdmin)
admin.site.register(Step)

