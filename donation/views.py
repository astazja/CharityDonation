from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import Institution, Donation, Category


class LandingPage(View):
    def get(self, request):
       bags = Donation.objects.all()
       num_institutions = Donation.objects.values('institution_id').distinct().count()
       institutions_list = Institution.objects.all()
       sum_bag = 0
       for bag in bags:
           sum_bag += bag.quantity
       context = {
           'bags': sum_bag,
           'institutions': num_institutions,
           'institutions_list':institutions_list
       }
       return render(request, 'index.html', context)

    # POPRAWIĆ html
    def listing(self, request):
        institution_list = Institution.objects.all()
        paginator = Paginator(institution_list, 5)
        page = request.GET.get('page')
        institutions_pag = paginator.get_page(page)
        return render(request, 'index.html', {'institutions_pag':institutions_pag})

    def logout_page(self, request):
        logout(request)
        return render(request, 'index.html')

class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {
            'categories':categories,
            'institutions': institutions
        }
        return render(request, 'form.html', context)

    def post(self,request):
        if request.user.is_authenticated:
            quantity = request.POST.get('bags')
            categories = request.POST.get('categories')
            institution = request.POST.get('organization')
            address = request.POST.get('address')
            phone_number =request.POST.get('phone')
            city = request.POST.get('city')
            zip_code = request.POST.get('postcode')
            pic_up_date = request.POST.get('date')
            pic_up_time = request.POST.get('time')
            pic_up_comment = request.POST.get('more_info')
            donation = Donation.objects.create(
                quantity=quantity,
                institution_id=institution,
                address=address,
                phone_number=phone_number,
                city=city,
                zip_code=zip_code,
                pic_up_date=pic_up_date,
                pic_up_time=pic_up_time,
                pic_up_comment=pic_up_comment
            )
            donation.save()
            donation.categories.add(categories)
        return redirect('/add/confirmation')

def get_institution_category(request):
    category_id = request.GET.getlist('category')
    istitution = Institution.objects.filter(categories__in = category_id)
    return render(request, 'institution.html', {'institutions':istitution})

class FormConfirmationView(View):
    def post(self, request):
        return render(request, 'form-confirmation.html')

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