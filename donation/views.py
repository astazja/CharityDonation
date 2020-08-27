from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Institution, Donation

class LandingPage(View):
    def get(self, request):
       bags = Donation.objects.all()
       num_institutions = Donation.objects.values('institution_id').distinct().count()
       institutions_list = Institution.objects.prefetch_related('categories__institution_set').all()
       sum_bag = 0
       for bag in bags:
           sum_bag += bag.quantity
       context = {
           'bags': sum_bag,
           'institutions': num_institutions,
           'institutions_list':institutions_list
       }
       return render(request, 'index.html', context)

    # POPRAWIĆ
    def listing(self, request):
        institution_list = Institution.objects.all()
        paginator = Paginator(institution_list, 5)
        page = request.GET.get('page')
        institutions_pag = paginator.get_page(page)
        return render(request, 'index.html', {'institutions_pag':institutions_pag})

class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

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