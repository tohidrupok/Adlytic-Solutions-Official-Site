from django.contrib import admin
from .models import Category, Package , Name


class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['category_name','group']   

    prepopulated_fields = {'slug': ('category_name',)}  

class PackageAdmin(admin.ModelAdmin):
    list_display = ['package_name', 'amount']
    filter_horizontal = ('category',)
 

admin.site.register(Name)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Package, PackageAdmin) 


