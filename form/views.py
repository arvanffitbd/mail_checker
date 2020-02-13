from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Form 
from .models import ip

from bottle import *
import random
import requests
import datetime



keys = [] # make a list to store keys in
def productkey(request):
    while True: # keep making a new product key if the key is already been used
        key = random.randrange(11111111111111111111, 99999999999999999999)
        if key in keys:
            continue
        else:
            break
        keys.append(str(key)) # add the key to the list of keys
        print('Your product key is: ' + str(key))  #tell the user their product key
    return render(request, 'productkey.html',{'key':str(key)})


def verify(request):
    if request.GET.get('key'):
        key = request.GET['key']
        if key in keys:
            keys.remove(key)
            print("This is work")
        else:
            print('This is not work')
    return render(request, 'verify.html')



def home(request):
    if request.method == "POST":
        if request.POST['email']:
            mail = Form()
            mail.email = request.POST['email']
            
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')
                get_ip= ip() #imported class from model
                get_ip.ip_address= ipaddress
                get_ip.pub_date = datetime.date.today() #import datetime
                get_ip.save()

            user_ip = ipaddress
            user_ip_list = ip.objects.all().filter(ip_address=user_ip)

            if len(user_ip_list) < 5:
                # !!!PUT YOUR API KEY HERE!!!
                api_key="Nkm3J7Fkaef4M10R1nIt4HpEx"
                email = mail.email
                j = requests.get("https://api.millionverifier.com/api/v3/?api="+api_key+"&"+"email="+email).json()
                c = j['resultcode']

                if c == 1:
                    print("this is work")
                    return render(request, 'home.html',{'success':'This is a valid email.'})
                elif c == 2:
                    return render(request, 'home.html',{'catch_all':'Catch All'})
                elif c == 3:
                    return render(request, 'home.html',{'unknown':'This is a Unknown email.'})
                elif c == 4:
                    return render(request, 'home.html',{'Error: ': j['error']})
                elif c == 5:
                    return render(request, 'home.html',{'disposable':'Disposable'})
                else:
                    return render(request, 'home.html',{'invalid':'This is a invalid email.'})
            else:
                return render(request, 'home.html',{'limit_over':'Limit Over.'})
        else:
            return render(request, 'home.html',{'no_field':'Field are required.'})

    else:
        return render(request, 'home.html')




    
@login_required(login_url="/accounts/signup")
def form(request):
    if request.method == "POST":
        if request.POST['email']:
            mail = Form()
            mail.email = request.POST['email']

            # !!!PUT YOUR API KEY HERE!!!
            api_key="Nkm3J7Fkaef4M10R1nIt4HpEx"
            email = mail.email
            j = requests.get("https://api.millionverifier.com/api/v3/?api="+api_key+"&"+"email="+email).json()
            c = j['resultcode']
            
            if c == 1:
                print("this is work")
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