from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from loginsignup.models import CustomUser

def login_user(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(req,'No registered email!')
            return redirect('login')
        elif email=='admin' and password=='Drc@1234':
            user = authenticate(req,email=email,password=password)
            login(req,user)
            return redirect('/adminpanel')
        else:
            user = authenticate(req,email=email,password=password)
            if user is None:
                messages.error(req,'Password is incorrect!')
                return redirect('login')
            else:
                login(req,user)
                return redirect(f'/user/{user.id}')
    return render(req,'login.html')


def signup_user(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        username = req.POST.get('username')
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')
        phone = req.POST.get('phone')
        address = req.POST.get('address')
        password = req.POST.get('password')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(req,'Email-Id already exists!')
            return redirect('signup')
        else:
            CustomUser.objects.create(
                email=email,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                password=password,
            )
            user = authenticate(req,email=email,password=password)
            if user is None:
                messages.error(req,'Password is incorrect!')
                return redirect('login')
            else:
                login(req,user)
                return redirect(f'/user/{user.id}')
    return render(req,'signup.html')

@login_required(login_url='/login/')
def adminlogin(req):
    return render(req,'adminhomepage.html')

@login_required(login_url='/login/')
def userhomepage(req,id):
    return render(req,'userhomepage.html',context={
        
    })