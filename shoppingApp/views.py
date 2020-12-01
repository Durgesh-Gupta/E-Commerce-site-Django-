from django.shortcuts import render,redirect,HttpResponse
from .models import UserForm,Category,Product,Cart
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    cl=Category.objects.all()
    pl=Product.objects.all()
    d={'cl':cl,'pl':pl}
    return render(request,'index.html',d)

def addUser(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        cl=Category.objects.all()
        f=UserForm
        d={'form':f,'cl':cl}
    return render(request,'form.html',d)

def bycategory(request,id):
    cl=Category.objects.all()
    pl=Product.objects.filter(Category_id=id)
    d={'cl':cl,'pl':pl}
    
    
    return render(request,'index.html',d)

from django.contrib.auth import login,logout,authenticate

def login_view(request):
    cl=Category.objects.all()
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            lmsg='INvalid Username or passowrd'
            d={'cl':cl,'lmsg':lmsg}
            return render(request,'login.html',d)

    else:
        d={'cl':cl}
        return render(request,'login.html',d)

def logout_view(request):
    logout(request)
    return redirect('/')



def searchproduct(request):
    cl=Category.objects.all()
    if request.method=='POST':
        sp=request.POST.get('sp')
        pl=Product.objects.filter(name__contains=sp)
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
    else:
        pl=Product.objects.all()
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
        

def addtocart(request,id):
    print("Product",id)
    prd=Product.objects.get(id=id)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    # print(prd.id,prd.name,prd.price)
    ct=Cart()
    ct.Product=prd
    ct.user=user
    ct.save()
    # print('----->',user.id,user.first_name)
    return redirect('/')

from .models import PlaceOrder
def cartlist(request):
    cl=Category.objects.all()
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    if request.method=='POST':
        bill=request.POST.get('totalb')
        op=PlaceOrder()
        op.user=user
        op.totalBill=int(bill)
        op.save()
        crlist=Cart.objects.filter(user=uid)
        for i in crlist:
            i.delete()
        return redirect('/')

    else:
        crlist=Cart.objects.filter(user=uid)

        cl=Category.objects.all()
    # pl=Product.objects.filter(Category_id=id)
        d={'cl':cl,'crlist':crlist}
        totalBill=0
        for i in crlist: 
            totalBill=totalBill+i.Product.price
        d['totalBill']=totalBill
    return render(request,'cartlist.html',d)

def orderlist(request):
    uid=request.session.get('uid')

    orlist=PlaceOrder.objects.filter(user=uid)
    cl=Category.objects.all()

    d={'cl':cl,'orlist':orlist}
    return render(request,'myorder.html',d)