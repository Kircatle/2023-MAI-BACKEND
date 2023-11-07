from django.contrib import admin

from .models import Incident, IncidentType

@admin.register(Incident)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(IncidentType)
class CompanyAdmin(admin.ModelAdmin):
    pass
