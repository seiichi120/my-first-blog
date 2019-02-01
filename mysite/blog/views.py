from django.shortcuts import render

from email.mime.text import MIMEText
import smtplib
from django.core.mail import EmailMessage
from django.http import HttpResponse
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def pay(request):
    d = {
        'your_name': request.GET.get('your_name'),
        'address': request.GET.get('address'),
    }

    e = d['address']
    if e:
        EmailMessage('test mail',d['your_name'] + ', Thanks!', to = [e]).send()

    return render(request, 'blog/pay.html', d)

def form(request):
    return render(request, 'blog/form.html')

def index(request):
    return render(request, 'blog/index.html')
