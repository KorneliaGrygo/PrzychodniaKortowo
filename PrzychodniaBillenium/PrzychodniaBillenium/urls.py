"""PrzychodniaBillenium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import A
from django.contrib import admin
from django.urls import path
from ClinicModule import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Przychodnia Kortowo - panel admina"
admin.site.site_title = "Przychodnia Kortowo - panel admina"
admin.site.index_title = "Witaj w przychodni Kortowo!"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('update-profile/', views.UpdateProfileView.as_view(), name='update-profile'),
    path('visits-calendar/', views.CalendarView.as_view(), name='calendar'),
    path('?', views.LogoutView.as_view(), name='logout'),

    path('patient/details/',views.PatientDetails.as_view(),name='patient-details'),
    path('patient/details/update',views.PatientUpdate.as_view(),name='patient-update'),
    path('register/regulations/',views.Regulations.as_view(),name='regulations'),
    path('register/privacy/',views.Privacy.as_view(),name='privacy'),
    path('informations/',views.Informations.as_view(),name='informations'),
    path('visits/',views.VisitView.as_view(),name='visit'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
