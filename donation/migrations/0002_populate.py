from django.db import migrations
from donation.models import Category, Institution

def populate(apps, schema_editor):
    Category.objects.create(name="zabawki")
    Category.objects.create(name="książki")
    Category.objects.create(name="ubrania, które nadają się do ponownego użycia")
    Category.objects.create(name="ubrania do wyrzucenia")
    Category.objects.create(name="ubrania z metką")
    Category.objects.create(name="buty")

    Institution.objects.create(name="Fundacja - Bez domu", description="Cel i misja. Pomoc dla osób nie posiadających miejsca zamieszkania", type="fun")
    Institution.objects.create(name="Fundacja - Dla dzieci", description="Cel i misja. Pomoc osobom znajdujacym się w trudniej sytuacji życiowej", type="fun")
    Institution.objects.create(name="Fundacja - Mam marzenie", description="Cel i misja. Pomoc osobom znajdujacym się w trudniej sytuacji życiowej", type="fun")
    Institution.objects.create(name="Fundacja - Zabawki",
                               description="Cel i misja. Pomoc dla osób potrzebujących zabawki",
                               type="fun")
    Institution.objects.create(name="Fundacja - Koce",
                               description="Cel i misja. Pomoc osobom potrzebujących kocy",
                               type="fun")
    Institution.objects.create(name="Fundacja - Bez butów",
                               description="Cel i misja. Pomoc osobom potrzebujących butów",
                               type="fun")

class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]