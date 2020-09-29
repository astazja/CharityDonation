from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views import View

from donation.models import Donation


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'error_message':'Twoje konto jest zablokowane.'})
        else:
            return render(request, 'register.html', {'error_message':'Taki użytkownik nie istnieje. Zarejestruj się.'})

class Logout(View):
    def get(self,request):
        logout(request)
        return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        try:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
        except(ValueError):
            return render(request, 'register.html', {'error_message':'Wypełnij poprawnie wszystkie pola.'})
        else:
            if name == '':
                return render(request, 'register.html', {'error_message': 'Pole imię nie może być puste.'})
            elif surname == '':
                return render(request, 'register.html', {'error_message': 'Pole nazwisko nie może być puste.'})
            elif email == '':
                return render(request, 'register.html', {'error_message': 'Pole email nie może być puste.'})
            elif password == '':
                return render(request, 'register.html', {'error_message': 'Pole hasło nie może być puste.'})
            else:
                if password == password2:
                    User.objects.create_user(first_name=name, last_name=surname, username=email, password=password)
                    return render(request, 'login.html')
                else:
                    return render(request, 'register.html', {'error_message': 'Hasła muszą być takie same.'})

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
        return render (request, 'profil.html', context)