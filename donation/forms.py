from django import forms
from .models import Donation, Category, Institution

class DateInputForm(forms.DateInput):
    input_type = 'date'

class TimeInputForm(forms.TimeInput):
    input_type = 'time'

class DonationForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'step':'1', 'min':'1'}))
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    institution = forms.ModelChoiceField(queryset=Institution.objects.all())
    pic_up_date = forms.DateField(widget=DateInputForm())
    pic_up_time = forms.TimeField(widget=TimeInputForm())
    pic_up_comment = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Donation
        fields = ['quantity', 'categories', 'institution', 'address', 'phone_number',
                  'city', 'zip_code', 'pic_up_date', 'pic_up_time', 'pic_up_comment']
