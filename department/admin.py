from django.contrib import admin
from .models import Category, Package , Name, PackageOrder , Portfolio, TeamMember , Client, Contact, Service


class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['category_name','group']   

    prepopulated_fields = {'slug': ('category_name',)}  

class PackageAdmin(admin.ModelAdmin): 
    list_display = ['package_name', 'amount']
    filter_horizontal = ('category',) 

    prepopulated_fields = {'functions': ('package_name',)}  

class PackageOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'package', 'contact')
    search_fields = ('name', 'package__name', 'email')

class ServiceAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug': ('name',)}    


admin.site.register(Name)
admin.site.register(Portfolio)
admin.site.register(TeamMember)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(PackageOrder,PackageOrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Package, PackageAdmin) 
admin.site.register(Service, ServiceAdmin) 


