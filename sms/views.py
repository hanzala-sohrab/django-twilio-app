from django.shortcuts import render
from .forms import SMSForm
from django.http import HttpResponseRedirect
from twilio.rest import Client

# Create your views here.
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


def index(request):
    print(request)
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            print("Hello")
            phone = "+91" + form.cleaned_data.get('phone')
            foo = form.cleaned_data.get('message')
            sms = {
                'phone': phone,
                'message': foo
            }
            print(sms)
            message = client.messages.create(
                to=phone,
                from_="+13072962585",
                body=foo
            )

            print(message.sid)
            return HttpResponseRedirect('/sent/')
    else:
        form = SMSForm()
    return render(request, 'send_sms.html')


def sent(request):
    return render(request, 'sent.html')
