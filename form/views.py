from django.shortcuts import render,redirect
from .models import Form 

import requests

def home(request):
    return render(request, 'home.html')

def form(request):
    if request.method == "POST":
        if request.POST['email']:
            mail = Form()
            mail.email = request.POST['email']

            # !!!PUT YOUR API KEY HERE!!!
            api_key="TKMDDluSNSOZhMxcTJzK6fLcZ"

            email = mail.email
            j = requests.get("https://api.millionverifier.com/api/v3/?api="+api_key+"&"+"email="+email).json()
            c = j['resultcode']
            
            if c == 1:
                return render(request, 'form.html',{'success':'This is a valid email.'})
            elif c == 2:
                return render(request, 'form.html',{'catch_all':'Catch All'})
            elif c == 3:
                return render(request, 'form.html',{'unknown':'This is a Unknown email.'})
            elif c == 4:
                return render(request, 'form.html',{'Error: ': j['error']})
            elif c == 5:
                return render(request, 'form.html',{'disposable':'Disposable'})
            else:
                return render(request, 'form.html',{'invalid':'This is a invalid email.'})
        else:
            return render(request, 'form.html',{'no_field':'Field are required.'})
    else:
        return render(request, 'form.html')