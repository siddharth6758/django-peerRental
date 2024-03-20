from django.db import models
from loginsignup.models import CustomUser
import random,string

def pk_generate():
    chars = string.ascii_uppercase+string.digits
    return ''.join(random.choices(chars,k=4))

RENT_TYPE = (
    ('/hour','/hour'),
    ('/day','/day'),
    ('/week','/week'),
    ('/month','/month'),
    ('/year','/year'),
)

class Products(models.Model):
    prod_id = models.CharField(max_length=4,primary_key=True)
    posted_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    rented_by = models.CharField(default='Not yet')
    posted_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    prod_img = models.FileField(upload_to='products/')
    prod_price = models.CharField()
    rent_type = models.CharField(default='/hour',choices=RENT_TYPE)
    
    def save(self,*args,**kwargs):
        if not self.prod_id:
            self.prod_id = pk_generate()
        super().save(*args, **kwargs)