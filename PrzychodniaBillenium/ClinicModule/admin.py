from django.contrib.auth import get_user_model
from ClinicModule import models
from django.contrib import admin


User = get_user_model()


# Register your models here.


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DrugPatient)
class DrugPatientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisitRecommendation)
class VisitRecommendationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Allergy)
class AllergyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DrugMedicine)
class DrugMedicineAdmin(admin.ModelAdmin):
    pass
