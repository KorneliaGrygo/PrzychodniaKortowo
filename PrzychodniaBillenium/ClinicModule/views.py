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

# Create your views here.
User = get_user_model()


class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse('In Construction!')


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


class RegisterView(View):

    template_name = 'register.html'
    form_class = custom_forms.CustomUserForm

    def get(self, request, *args, **kwargs):
        form_register = self.form_class()
        return render(request, self.template_name, {'form_register': form_register})

    def post(self, request, *args, **kwargs):
        form_register = self.form_class(request.POST)
        if form_register.is_valid():
            email = form_register.cleaned_data.get('email')
            first_name = form_register.cleaned_data.get('first_name')
            second_name = form_register.cleaned_data.get('second_name')
            phone_number = form_register.cleaned_data.get('phone_number')
            password = form_register.cleaned_data.get('password')

            user = User.objects.create(email=email, first_name=first_name,
                                       second_name=second_name, phone_number=phone_number, password=password)
            user.save()

            # return here to the main view
            return redirect('home')

        else:
            forms.ValidationError(request, _(
                'Pola są nieprawidłowe.'))
        return render(request, self.template_name, {'form_register': form_register})
