from django.db import migrations
from donation.models import Donation

def populate(apps, schema_editor):
    Donation.objects.create(quantity=2, address="Prosta 51/3", phone_number=606334234, city="Warszawa",
                            zip_code="99-098",
                            pic_up_date="2020-09-24", pic_up_time="15:40",
                            pic_up_comment="Pierwsze piętro, mieszkanie po lewej od klatki schodowej", institution_id=1)
    Donation.objects.create(quantity=4, address="Zielona 23", phone_number=260436334, city="Warszawa",
                            zip_code="90-125",
                            pic_up_date="2020-10-04", pic_up_time="16:40",
                            pic_up_comment="Proszę nie dzwonić domofonem",
                            institution_id=2)
    Donation.objects.create(quantity=3, address="Kazimierowa 5/139", phone_number=346063234, city="Mińsk Mazowiecki",
                            zip_code="84-048", pic_up_date="2020-10-11", pic_up_time="17:30",
                            pic_up_comment="Trzecie piętro, brak windy", institution_id=3)

class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_populate'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]