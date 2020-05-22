from django import forms
from accounts.models import UserProfile

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=255)
    address_2 = forms.CharField(max_length=150)
    contact = forms.IntegerField(min_value=0)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        profile = UserProfile()
        profile.address = self.cleaned_data['address']
        profile.address_2= self.cleaned_data['address_2']
        profile.contact = self.cleaned_data['contact']
        user.save()
        profile.user = user
        profile.save()