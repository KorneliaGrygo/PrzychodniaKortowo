
from django.contrib.auth import get_user_model
from ClinicModule import models
from django.contrib import admin
from django.contrib.auth.models import Group


User = get_user_model()

admin.site.unregister(Group)
# Register your models here.


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('person', 'address', 'city', 'PESEL', 'email', 'phone', )
    list_filter = ('user', )
    search_fields = ('user__first_name','user__second_name','address','city',)

    def person(self,obj):
        return f'{obj.user.first_name} {obj.user.second_name}'
    def email(self,obj):
        return obj.user.email
    def phone(self,obj):
        return obj.user.phone_number
   


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'specialization')


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('first_name','second_name', 'doctor', 'category',
                    'visit_day_start', 'visit_time_start', 'visit_time_end',)

    search_fields = ('patient__user__first_name','patient__user__second_name','doctor__first_name','doctor__second_name')

    def first_name(self,obj):
        return obj.patient.user.first_name

    def second_name(self,obj):
        return obj.patient.user.second_name
  


@admin.register(models.DrugPatient)
class DrugPatientAdmin(admin.ModelAdmin):

    list_display = ('person', 'doctor','visitdate', 'drug',)
    
    def person(self,obj):
        return f'{obj.patient.user.first_name} {obj.patient.user.second_name}'
    def visitdate (self,obj):
        return f'{obj.visit.visit_day_start} '


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisitRecommendation)
class VisitRecommendationAdmin(admin.ModelAdmin):
    list_display = ('patient','category','doctor','date_added',)

    def patient(self,obj):
        return f'{obj.visit.patient.user.first_name} {obj.visit.patient.user.second_name}'
    def date_added(self,obj):
        return obj.visit.date_added
    def category(self,obj):
        return obj.visit.category
    def doctor(self,obj):
        return f'Dr.{obj.visit.doctor.first_name} {obj.visit.doctor.second_name}'


@admin.register(models.Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('person', 'allergy_type', 'allergens_type',)
    search_fields = ('patient__user__first_name','allergy_type',)
    def person(self,obj):
        return f'{obj.patient.user.first_name} {obj.patient.user.second_name}'


@admin.register(models.DrugMedicine)
class DrugMedicineAdmin(admin.ModelAdmin):
    list_display = ('drug_title', 'description_of_drug')
    search_fields = ('drug_title',)
