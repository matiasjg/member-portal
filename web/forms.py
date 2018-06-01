from django import forms
from core.models import Plan

class SignupForm(forms.Form):
    member_email = forms.EmailField(label='Email')
    member_fname = forms.CharField(label='First Name', max_length=200)
    member_lname = forms.CharField(label='Last Name', max_length=200)
    plan         = forms.ModelChoiceField(label='Select Plan', queryset=Plan.objects.all())

    member_email.widget.attrs.update({'class': 'form-control'})
    member_fname.widget.attrs.update({'class': 'form-control'})
    member_lname.widget.attrs.update({'class': 'form-control'})
    plan.widget.attrs.update({'class': 'form-control'})

class PayForm(forms.Form):
    member_email = forms.EmailField(label='Member Email')
    payment_amount = forms.DecimalField(label='Payment Amount')

    member_email.widget.attrs.update({'class': 'form-control'})
    payment_amount.widget.attrs.update({'class': 'form-control'})


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200)

    search.widget.attrs.update({'class': 'form-control mr-sm-2', 'placeholder': 'Search Member'})
