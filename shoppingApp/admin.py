from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cname']
    list_filter=['cname']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','desc','Category']
    list_filter=['name','price','Category']


admin.site.register(Product,ProductAdmin)