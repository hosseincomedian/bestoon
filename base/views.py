from django.shortcuts import render
from .models import dakhl
# Create your views here.
def home(request):
        a=dakhl.objects.all()
        for i in range(1,len(a)):
            if (a[i].date == a[i-1].date):
                a[i].date=""
        return render(request,'home.html')