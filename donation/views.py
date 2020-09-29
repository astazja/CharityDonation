import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .forms import DonationForm
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

class AddDonation(View):
    def get(self, request):
        form = DonationForm()
        if request.user.is_authenticated:
            categories = dict()
            for category in Category.objects.all():
                categories[category.id] = [institution.id for institution in Institution.objects.filter(categories=category.id)]
            categories_for_js = json.dumps(categories)
            context = {
                'form':form,
                'categories':categories_for_js
            }
            return render(request, 'form.html', context)

        return redirect('url_login')

    def post(self,request):
        form = DonationForm(request.POST)
        data = dict()
        if form.is_valid():
            donation = form.save()
            donation.user = request.user
            form.save()
            data['form_is_vaild'] = True
        else:
            data['form_is_vaild'] = False
        return JsonResponse(data)

class FormConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')