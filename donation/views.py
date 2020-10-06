import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View, generic

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
def listing( request, institution_type, page_number):
    institution_list = Institution.objects.filter(type=institution_type)
    paginator = Paginator(institution_list, 5)
    page = request.GET.get(f"{page_number}",1)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)
    return records

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

class ArchiveDonation(LoginRequiredMixin, View):
    def get(self, request, donation_id):
        raise Http404('Archiwizacja możliwa tylko poprzez przycisk w szczególe widoku darowizny')

    def post(self, request, donation_id):
        donation = get_object_or_404(Donation, id=donation_id)
        donation.is_taken = False if donation.is_taken else True
        donation.save()
        return redirect('url_profile')

class SingleDonation(LoginRequiredMixin, generic.DetailView):
    model = Donation
    context_object_name = 'donation'


