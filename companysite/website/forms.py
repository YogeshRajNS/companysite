from django import forms

class formss(forms.Form):
    name= forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)
    mobile_number=forms.CharField(min_length=10)