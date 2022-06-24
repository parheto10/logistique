from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Gps,Sortiequipement, Accessoire,Ordinateur,Imprimante

# Register your models here.
class GpsAdmin(ImportExportModelAdmin):
    list_display = ['code', 'marque', 'model', 'prix_achat']

class SortiequipementAdmin(ImportExportModelAdmin):
    fields = ['gps', 'technicien', 'projet',  'accessoires']
    list_display = ['gps', 'technicien', 'projet']

admin.site.register(Ordinateur)
admin.site.register(Imprimante)
admin.site.register(Accessoire)
admin.site.register(Gps, GpsAdmin)
admin.site.register(Sortiequipement, SortiequipementAdmin)