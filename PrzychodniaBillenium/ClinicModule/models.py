from . import validators
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


class VisitCategory(models.TextChoices):

    INITIAL = 'Initial visit', _('Initial visit')
    CONTROL = 'Control visit', _('Control visit')
    TREATMENT = 'Treatment', _('Symptomatic treatment')


class Patient(models.Model):
    """
            Class defines the patient,
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    PESEL = models.CharField(validators=[validators.validate_patient_pesel],
                             max_length=11, unique=True,
                             help_text=_('Enter the PESEL identificator: '))

    address = models.CharField(_('Address'), max_length=64)

    city = models.CharField(_('City'), max_length=64, default='Olsztyn')

    zip_code = models.CharField(validators=[validators.validate_zip_code],
                                help_text=_('Zip code'), max_length=5, default="10117")

    # Represents the Patient object as second name with PESEL ID.

    def __str__(self):
        return f'{self.user.second_name} - {self.PESEL}'


class Doctor(models.Model):
    """
            Model represents the doctor
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(
        max_length=32,
        choices=Specialization.choices,
        default=Specialization.INTERNIST
    )

    # Order Doctors by ID
    class Meta:
        ordering = [
            'id'
        ]

    # Description about their proffession, career etc.
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'Dr. {self.user.first_name} {self.user.second_name}'


class Visit(models.Model):
    """
    Visit model for patients
    """

    identificator = models.SlugField(
        default=validators.get_random_secret,
        max_length=12,
        unique=True,
        editable=False,
        blank=False
    )

    date_added = models.DateTimeField(
        _("Date and time of creation the visit."),
        auto_now_add=True)

    date_modified = models.DateTimeField(
        _('Date and time of modification the visit.'),
        null=True,
        blank=True,
        editable=True
    )

    # Short description of visit
    description = models.CharField(
        _('Short description (purpose) of the visit.'),
        max_length=500,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.RESTRICT
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.RESTRICT
    )

    category = models.CharField(
        max_length=32,
        choices=VisitCategory.choices,
        default=VisitCategory.INITIAL
    )

    def __str__(self):
        return f'ID: {self.identificator}'

    class Meta:
        ordering = [
            'date_added',
            'patient'
        ]
