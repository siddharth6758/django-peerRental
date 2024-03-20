from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.forms import ProductFrom
from django.contrib import messages

@login_required(login_url='/login/')
def uploadproduct(req):
    forms = ProductFrom()
    if req.method == 'POST':
        forms = ProductFrom(req.POST,req.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(req,'Product uploaded successfully!')
            return redirect(f'/user/{req.user.id}')
        else:
            messages.error(req,'Error occured while uploading product!')
            return redirect('/uploadproduct')
    return render(req,'uploadprod.html',context={
        'id':req.user.id,
        'forms':forms,
    })