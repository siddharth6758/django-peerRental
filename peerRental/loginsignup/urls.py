from django.urls import path
import loginsignup.views as lsv

urlpatterns = [
    path('login/',lsv.login_user,name='login'),
    path('signup/',lsv.signup_user,name='signup'),
    path('adminpanel/',lsv.adminlogin,name='adminlogin'),
    path('user/<int:id>',lsv.userhomepage,name='userhome'),
]
