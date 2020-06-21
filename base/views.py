from django.shortcuts import render
from .models import dakhl
# Create your views here.
def home(request):
    if request.method == "POST":
        mizan=int(request.POST['mizan'])
        tozih=request.POST['tozih']
        a=dakhl.objects.all()
        fe=codee=int(a[len(a)-1].darayi)
        darayi=fe+mizan
        a=dakhl.objects.all()
        dakhl.objects.create(mizan=mizan,darayi=darayi,tozih=tozih)
        return render(request,'home.html',{'dakhl':a})
    else:
        a=dakhl.objects.all()
        for i in range(1,len(a)):
            if (a[i].date == a[i-1].date):
                a[i].date=""
        return render(request,'home.html',{'dakhl':a})