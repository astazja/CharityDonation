# Generated by Django 3.1 on 2020-08-23 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('fun', 'fundacja'), ('non_gov_org', 'organizacja pozarządowa'), ('loc_coll', 'zbiórka lokalna')], default='fun', max_length=50)),
                ('categories', models.ManyToManyField(to='donation.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=6)),
                ('pic_up_date', models.DateField()),
                ('pic_up_time', models.TimeField()),
                ('pic_up_comment', models.TextField(blank=True)),
                ('categories', models.ManyToManyField(to='donation.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]