import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.
# Get the active user model - the custom model of User
User = get_user_model()

class Specialization(models.TextChoices):

    INTERNIST = 'Internist', _('Internist'),
    GASTROLOGIST = 'Gastrologist', _('Gastrologist'),
    OPHTHALMOLOGIST = 'Ophthalmologist', _('Ophthalmologist'),
    PULMONOLOGIST = 'Pulmonologist', _('Pulmonologist')


class Patient(models.Model):
    """
            Class defines the patient,
    """
    user = models.OnetToOneField(
        User,
        on_delete=models.CASCADE)

    PESEL = models.CharField(validators=[validators.validate_patient_pesel],
                             max_length=11, unique=True,
                             help_text=_('Enter the PESEL identificator: '))

    address = models.CharField(_('Address'), max_length=64)

    city = models.CharField(_('City'), max_length=64, defualt='Olsztyn')

    zip_code = models.CharField(validators=[validators.validate_zip_code],
                                help_text=_('Zip code'), max_length=5, default="10117")

    # Represents the Patient object as second name with PESEL ID.

    def __str__(self):
        return f'{self.user.second_name} - {self.PESEL}'


class Doctor(models.Model):
    """
            Model represents the doctor
    """

    user = models.OnetToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(
        max_length=32,
        choices=Specialization.choices,
        default=Specialization.INTERNIST
    )

    description = models.CharField(max_length=550)
