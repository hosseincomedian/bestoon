from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from base import views
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from base.models import dakhl
from django.http import HttpRequest
def sign_In(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                User.objects.get(username=username)
                tts={}
                tts['error']=" نام کاربری تکراری است"
                return render (request,'sign_in.html',tts)
            except Exception:
                User.objects.create_user(username=username, password=password)
                return render (request,'home.html')
    else:
        return render (request,'sign_in.html')


def log(request):
    return render(request,'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render (request,'home.html')

def profile(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            a= user.dakhl_set.all()
            for i in range(1,len(a)):
                if a[i].date == a[i-1].date:
                    a[i].date=""
                if a[i].darayi == a[i-1].darayi:
                    a[i-1].darayi = ""
                if a[i].mizan_dolar == a[i-1].mizan_dolar:
                    a[i-1].mizan_dolar = ""
            for i in range(0,len(a)):
                a[i].date=str(a[i].date)
                a[i].tozih=str(a[i].tozih)
                a[i].tozih=a[i].tozih.replace(' ', "_")
                if a[i].mizan==0:
                    a[i].mizan=""
                if a[i].dolar==0:
                    a[i].dolar=""
                if a[i].tozih=="":
                    a[i].tozih="-"
                

            return render(request,'profile.html',{'dakhl':a})   
        else:
            return (request,'login.html',{'error':'.اشتباه است لطفا دوباره تلاش کنید'})            
    else:
        if request.user.is_authenticated:
            a= request.user.dakhl_set.all()
            for i in range(1,len(a)):
                if a[i].date == a[i-1].date:
                    a[i].date=""
                if a[i].darayi == a[i-1].darayi:
                    a[i-1].darayi = ""
                if a[i].mizan_dolar == a[i-1].mizan_dolar:
                    a[i-1].mizan_dolar = ""
            for i in range(0,len(a)):
                a[i].date=str(a[i].date)
                a[i].tozih=str(a[i].tozih)
                a[i].tozih=a[i].tozih.replace(' ', "_")
                if a[i].tozih=="":
                    a[i].tozih="-"
                if a[i].mizan==0:
                    a[i].mizan=""
                if a[i].dolar==0:
                    a[i].dolar="" 
            
            return render(request,'profile.html',{'dakhl':a})
        else:
            return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render (request,'home.html')

def add(request):
    if (request.user.is_authenticated) ==0:
         return render(request,'login.html')
    if request.method == "POST":
        mizan=int(request.POST['mizan'])
        dolar=int(request.POST['dolar'])
        tozih=request.POST['tozih']
        a=dakhl.objects.all()
        fe=int(a[len(a)-1].darayi)
        do=int(a[len(a)-1].mizan_dolar)
        darayi=fe+mizan
        mizan_dolar = do+dolar
        a=User().dakhl_set.all()
        dakhl.objects.create(user=request.user,mizan=mizan,darayi=darayi,tozih=tozih,dolar=dolar,mizan_dolar=mizan_dolar)
        requestt = HttpRequest()
        return HttpResponseRedirect('/account/Profile')


