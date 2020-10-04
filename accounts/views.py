from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from accounts.forms import UserAuthenticationForm, UserRegisterForm, ChangePasswordForm

from donation.models import Donation


class Login(View):
    def get(self, request):
        form = UserAuthenticationForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request):
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
        messages.error(request, 'Błędnie podany email lub hasło.')
        return render(request, 'login.html', {'form':form})

class Logout(View):
    def get(self,request):
        logout(request)
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_login')
        return render(request, 'register.html', {'form':form})

class ProfilView(View):
    def get(self, request):
        sum_bag = 0
        if request.user.is_authenticated:
            donations = Donation.objects.filter(user_id = request.user.id)
            for don in donations:
                sum_bag += don.quantity
        context = {
            'donations': donations,
            'bags': sum_bag,
        }
        return render(request, 'profil.html', context)

class ChangePassword(View):
    def get(self,request):
        form = ChangePasswordForm(request.user)
        return render(request, 'change-profile.html', {'form':form})

    def post(self, request):
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Udało sie zmienić hasło. Proszę zalogować się ponownie, nowym hasłem.')
            return redirect('url_login')
        return render(request, 'change-profile.html', {'form':form})