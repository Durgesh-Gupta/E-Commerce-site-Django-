from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserInfo(User):
    age=models.IntegerField()
    contact=models.CharField(max_length=20)


class Category(models.Model):
    cname=models.CharField(max_length=50)
    def __str__(s):
        return s.cname


class Product(models.Model):
    name=models.CharField(max_length=25)
    price=models.IntegerField()
    img=models.ImageField(default="")
    desc=models.TextField(max_length=100)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(s):
        return s.name



from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','contact','email','password1','password2']

class Cart(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class PlaceOrder(models.Model):
    totalBill=models.IntegerField()
    orderDate=models.DateField(auto_now=True)
    status=models.CharField(max_length=30,default='Processing')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # img=models.ImageField(upload_to='images',default='')
