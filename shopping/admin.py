from django.contrib import admin
from .models import *

# Register your models here.
class catagdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catagdmin)

class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodAdmin)
class orderAdmin(admin.ModelAdmin):
    list_display = ['name','productname','phonenumber','orderdate','orderon']
admin.site.register(order,orderAdmin)
