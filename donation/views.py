from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Institution, Donation

class LandingPage(View):
    def get(self, request):
       bags = Donation.objects.all()
       num_institutions = Institution.objects.count()
       sum_bag = 0
       for bag in bags:
           sum_bag += bag.quantity
       context = {
           'bags': sum_bag,
           'institutions': num_institutions
       }
       return render(request, "index.html", context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")

class Login(View):
    def get(self, request):
        return render(request,"login.html")

class Register(View):
    def get(self, request):
        return render(request, "register.html")