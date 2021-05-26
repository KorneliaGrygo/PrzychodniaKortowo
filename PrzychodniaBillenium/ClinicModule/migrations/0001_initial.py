# Generated by Django 3.1.7 on 2021-05-26 21:53

import ClinicModule.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('second_name', models.CharField(max_length=64)),
                ('specialization', models.CharField(choices=[('Internist', 'Internist'), ('Gastrologist', 'Gastrologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Pulmonologist', 'Pulmonologist')], default='Internist', max_length=32)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['second_name', 'specialization'],
            },
        ),
        migrations.CreateModel(
            name='DrugMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=128)),
                ('description_of_drug', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['drug'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PESEL', models.CharField(help_text='Enter the PESEL identificator: ', max_length=11, unique=True, validators=[ClinicModule.validators.validate_patient_pesel])),
                ('address', models.CharField(max_length=64, verbose_name='Address')),
                ('city', models.CharField(default='Olsztyn', max_length=64, verbose_name='City')),
                ('zip_code', models.CharField(default='10117', help_text='Zip code', max_length=5, validators=[ClinicModule.validators.validate_zip_code])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificator', models.SlugField(default=ClinicModule.validators.get_random_secret, editable=False, max_length=12, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date and time of creation the visit.')),
                ('date_modified', models.DateTimeField(blank=True, null=True, verbose_name='Date and time of modification the visit.')),
                ('visit_day_start', models.DateField(blank=True, default=datetime.date.today)),
                ('visit_time_start', models.TimeField(blank=True, null=True)),
                ('visit_time_end', models.TimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Short description (purpose) of the visit.')),
                ('category', models.CharField(choices=[('Initial visit', 'Initial visit'), ('Control visit', 'Control visit'), ('Treatment', 'Symptomatic treatment')], default='Initial visit', max_length=32)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ClinicModule.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ClinicModule.patient')),
            ],
            options={
                'ordering': ['date_added', 'patient'],
            },
        ),
        migrations.CreateModel(
            name='VisitRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClinicModule.visit')),
            ],
        ),
        migrations.CreateModel(
            name='DrugPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClinicModule.doctor')),
                ('drug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drug_assigned', to='ClinicModule.drugmedicine')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ClinicModule.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_type', models.CharField(blank=True, choices=[('Food allergy', 'Food allergy'), ('Inhalation allergy', 'Inhalation allergy'), ('Contact Allergy', 'Contact Allergy'), ('Injection allergy', 'Injection allergy')], max_length=64)),
                ('allergens_type', models.CharField(blank=True, choices=[('Plant Allergens', 'Plant allergens'), ('Animal Allergens', 'Animal allergens'), ('Chemical Allergens', 'Chemical allergens')], max_length=64)),
                ('allergy_descrption', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClinicModule.patient')),
            ],
        ),
    ]
