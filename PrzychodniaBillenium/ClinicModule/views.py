from urllib.parse import urlparse
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from ClinicModule import models
from ClinicModule import forms as custom_forms
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.db.utils import IntegrityError

# Create your views here.
User = get_user_model()


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class CalendarView(TemplateView):
    template_name = 'fullcalendar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class LoginView(View):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        # Validate the form data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                forms.ValidationError(
                    request, _("Login lub hasło jest nieprawidłowe."))
        else:
            forms.ValidationError(request, _(
                "Login lub hasło jest nieprawidłowe."))
        return render(request, self.template_name, {'form': form})


class UpdateProfileView(View):

    template_name = 'update_profile.html'
    form_class = custom_forms.PatientForm

    def get(self, request, *args, **kwargs):
        referer = request.META.get('HTTP_REFERER')
        o = urlparse(referer)
        if request.user.is_authenticated and o.path == r'/register/':
            update_form = self.form_class()
            return render(request, self.template_name, {'update_form': update_form})
        else:
            return HttpResponse('Nie masz dostępu do tego zasobu.', status=401)

    def post(self, request, *args, **kwarsgs):
        referer = request.META.get('HTTP_REFERER')
        o = urlparse(referer)
        if self.request.user.is_authenticated and o.path == r'/update-profile/':
            update_form = self.form_class(request.POST)
            if update_form.is_valid():
                PESEL = update_form.cleaned_data.get('PESEL')
                address = update_form.cleaned_data.get('address')
                city = update_form.cleaned_data.get('city')
                zip_code = update_form.cleaned_data.get('zip_code')

                user_from_request = self.request.user.id

                if models.Patient.objects.filter(PESEL__exact=PESEL).exists():
                    raise forms.ValidationError(
                        _('Podany PESEL już istnieje!'), code='invalid')

                if not models.User.objects.filter(id=user_from_request).exists():
                    raise forms.ValidationError(
                        _('Wystąpił błąd, spróbuj ponownie później.'), code='invalid')

                user = models.User.objects.get(id=user_from_request)

                # create a patient based on authenticated user from request
                patient = models.Patient.objects.create(
                    user_id=user.id, PESEL=PESEL, address=address.title(), city=city.title(), zip_code=zip_code)

                try:
                    patient.save()
                except IntegrityError as e:
                    error_message = str(e.__cause__)

                # if operation is succesfull, return the approperiate message
                return redirect('home')
            else:
                forms.ValidationError(
                    request, _("Podane dane są nieprawidłowe."))
            return render(request, self.template_name, {'update_form': update_form})
        else:
            return HttpResponse('Nie masz dostępu.', status=401)


class RegisterView(View):

    template_name = 'register.html'
    form_class = custom_forms.CustomUserForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            form_register = self.form_class()
            return render(request, self.template_name, {'form_register': form_register})
        else:
            return HttpResponse('Posiadasz już konto.')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            form_register = self.form_class(request.POST)
            if form_register.is_valid():
                email = form_register.cleaned_data.get('email')
                first_name = form_register.cleaned_data.get('first_name')
                second_name = form_register.cleaned_data.get('second_name')
                phone_number = form_register.cleaned_data.get('phone_number')
                password = form_register.cleaned_data.get('password')

                user = User.objects.create_user(email=email, first_name=first_name.title(),
                                                second_name=second_name.title(), phone_number=phone_number, password=password)
                try:
                    user.save()
                except IntegrityError:
                    return render(request, self.template_name, {"message": 'User już istnieje!'})

                if User.objects.filter(id=user.id).exists():
                    user = authenticate(username=email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('update-profile')
                    else:
                        return HttpResponse('Nastąpił błąd podczas uwierzytelniania użytkownika do systemu.', status=400)
                else:
                    return HttpResponse('Podczas rejestracji wystąpił błąd.', code=400)

                # return here to the update profile user
                return redirect('update-profile')

            else:
                forms.ValidationError(request, _(
                    'Pola są nieprawidłowe.'))
            return render(request, self.template_name, {'form_register': form_register})
