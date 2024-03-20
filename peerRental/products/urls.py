from django.urls import path
import products.views as pv

urlpatterns = [
    path('uploadproduct/',pv.uploadproduct,name='uploadproduct'),
]
