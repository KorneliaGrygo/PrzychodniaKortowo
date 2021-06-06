from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from ClinicModule import models
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})


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
                    request, "Invalid username or password.")
        else:
            forms.ValidationError(request, "Invalid username or password.")
        return render(request, self.template_name, {'form': form})
