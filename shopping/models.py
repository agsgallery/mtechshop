from django.db import models
from django.db.models import CASCADE
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prodt_cat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])



    def __str__(self):
        return '{}'.format(self.name)

class order(models.Model):
    name=models.CharField(max_length=100)
    productname=models.ForeignKey(products,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=100)
    orderdate=models.DateField()
    orderon=models.DateField(auto_now=True)



# Create your models here.
