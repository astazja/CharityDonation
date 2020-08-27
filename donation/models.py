from django.db import models
from django.contrib.auth.models import User

# Create your models here.
FUNDATIONS = (
    ("fun", "fundacja"),
    ("non_gov_org", "organizacja pozarządowa"),
    ("loc_coll", "zbiórka lokalna")
)

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    type = models.CharField(choices=FUNDATIONS, max_length=50, default="fun")
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=6)
    pic_up_date = models.DateField()
    pic_up_time = models.TimeField()
    pic_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)