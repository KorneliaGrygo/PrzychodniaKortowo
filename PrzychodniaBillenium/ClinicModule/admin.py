from django.contrib import admin
from ClinicModule.models import Test

# Register your models here.


@admin.register(Test)
class AuthorAdmin(admin.ModelAdmin):
    pass
