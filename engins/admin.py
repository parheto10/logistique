from django.contrib import admin
from .models import Chauffeur, Vehicule, Moto, Course, Detail_Course, Mission, detail_mission, Escale

class DetailCourseAdmin(admin.TabularInline):
   model = Detail_Course
   extra = 0

class DetailMissionAdmin(admin.TabularInline):
   model = detail_mission
   extra = 0

class EscaleAdmin(admin.TabularInline):
   model = Escale
   extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [DetailCourseAdmin]

class MissionAdmin(admin.ModelAdmin):
    inlines = [DetailMissionAdmin, EscaleAdmin]

class VehiculeAdmin(admin.ModelAdmin):
    list_display = ['matricule', 'marque', 'model', 'projet', 'couleur']
    list_filter = ['projet__sigle', 'marque',]

class MotoAdmin(admin.ModelAdmin):
    list_display = ['matricule', 'responsable', 'projet', 'marque', 'model', 'type']
    list_filter = ['projet__sigle', 'type',]

class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenoms', 'contact1', 'contact2']
    # list_filter = ['projet__sigle', 'type',]

admin.site.register(Chauffeur, ChauffeurAdmin)
admin.site.register(Vehicule, VehiculeAdmin)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Course, CourseAdmin)
# admin.site.register(Detail_Course)
admin.site.register(Mission, MissionAdmin)
# admin.site.register(detail_mission)
# admin.site.register(Escale)

# Register your models here.
