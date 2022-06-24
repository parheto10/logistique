from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Responsable, Projet, Technicien

class ResponsableAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nom', 'prenoms', 'poste', 'contact1', 'email_pro']

class ProjetAdmin(ImportExportModelAdmin):
    list_display = ['id', 'sigle', 'titre', 'chef', 'debut', 'fin', 'etat']

class TechnicienAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nom', 'prenoms', 'localite', 'projet', 'contact1', 'poste']

admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Technicien, TechnicienAdmin)

# Register your models here.
