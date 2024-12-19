# forms.py
from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    agree_to_terms = forms.BooleanField(required=True)