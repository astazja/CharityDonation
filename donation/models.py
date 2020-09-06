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
    name = models.CharField(max_length=120, verbose_name="Nazwa")
    description = models.TextField(blank=True, verbose_name="Opis")
    type = models.CharField(choices=FUNDATIONS, max_length=50, default="fun", verbose_name="Typ")
    categories = models.ManyToManyField(Category, verbose_name="Kategorie")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Instytucja"
        verbose_name_plural = "Instytucje"

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