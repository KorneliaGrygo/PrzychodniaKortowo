from . import validators
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.forms import ModelForm

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
        return f'{self.user.second_name}'


class Doctor(models.Model):
    """
            Model represents the doctor
    """

    first_name = models.CharField(
        max_length=64,
        blank=False,
        null=False
    )

    second_name = models.CharField(max_length=64,
                                   blank=False,
                                   null=False)

    specialization = models.CharField(
        max_length=32,
        choices=Specialization.choices,
        default=Specialization.INTERNIST
    )

    # Order Doctors by ID
    class Meta:
        ordering = [
            'second_name',
            'specialization'
        ]

    # Description about their proffession, career etc.
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'Dr. {self.first_name} {self.second_name}'


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

    visit_day_start = models.DateField(default=date.today, blank=True)
    visit_time_start = models.TimeField(null=True, blank=True)
    visit_time_end = models.TimeField(null=True, blank=True)

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
        return f'ID: {self.identificator}, Patient: {self.patient.user.second_name}, Doctor: {self.doctor.second_name}'

    class Meta:
        ordering = [
            'date_added',
            'patient'
        ]


class DrugPatient(models.Model):

    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    drug = models.ForeignKey('DrugMedicine',
                             related_name='drug_assigned',
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient}'


class VisitRecommendation(models.Model):
    """
        Model class for recommendations about the patient visit
    """
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)

    # Description of the recommendation
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.visit.identificator}, {self.visit.patient}, {self.visit.date_added.strftime("%Y-%m-%d %H:%M:%S")}'


class DrugMedicine(models.Model):

    drug_title = models.CharField(max_length=128, blank=False)
    description_of_drug = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return f'{self.drug_title}'

    class Meta:
        ordering = [
            'drug_title'
        ]


class Allergy(models.Model):

    TYPE_ALLERGY = [
        ('Food allergy', _('Food allergy')),
        ('Inhalation allergy', _('Inhalation allergy')),
        ('Contact Allergy', _('Contact Allergy')),
        ('Injection allergy', _('Injection allergy'))
    ]

    ALLERGENS = [
        ('Plant Allergens', _('Plant allergens')),
        ('Animal Allergens', _('Animal allergens')),
        ('Chemical Allergens', _('Chemical allergens'))
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergy_type = models.CharField(
        max_length=64, blank=True,
        choices=TYPE_ALLERGY)

    allergens_type = models.CharField(max_length=64, blank=True,
                                      choices=ALLERGENS)

    allergy_descrption = models.TextField()

    def __str__(self):
        return f'{self.patient.PESEL} - {self.patient.user.second_name} - Type: {self.allergy_type}, Category: {self.allergens_type}'


class PatientForm(ModelForm):

    class Meta:
        model = Patient
        fields = [
            'user',
            'PESEL',
            'address',
            'city',
            'zip_code'
        ]
