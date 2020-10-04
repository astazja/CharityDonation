"""CharityDonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from donation.views import LandingPage,AddDonation, FormConfirmationView
from accounts.views import Login, Logout, Register, ProfilView, ChangePassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name="url_landing_page"),
    path('add/', AddDonation.as_view(), name="url_add_donation"),
    path('login/', Login.as_view(), name="url_login"),
    path('logout/', Logout.as_view(), name="url_logout"),
    path('register/', Register.as_view(), name="url_register"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profil/', ProfilView.as_view(), name="url_profil"),
    path('add/confirmation/', FormConfirmationView.as_view(), name="url_confirmation"),
    path('profil/change/', ChangePassword.as_view(), name="url_change"),
]
