from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class dakhl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    mizan=models.IntegerField()
    date = models.DateField(auto_now_add=True)
    darayi = models.BigIntegerField()
    tozih = models.CharField(max_length=500, blank=True)