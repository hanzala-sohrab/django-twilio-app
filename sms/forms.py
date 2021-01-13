from django import forms


class SMSForm(forms.Form):
    phone = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
