from django.shortcuts import render, get_object_or_404
from .models import Category, Package

# Create your views here.
def home(request):  
    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    package = Category.objects.filter(group__part="package")

    context = {'service': service, 'softwear': softwear, 'package': package}  

    return render(request, 'home.html', context) 


def details(request, category_slug=None):
    context = {}  
   
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        
        all_pakg = Package.objects.filter(category=category) 

    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    package = Category.objects.filter(group__part="package")

    context = {'category': category, 'package': package, 'service': service, 'softwear': softwear, 'all_pakg': all_pakg}


    return render(request, 'details.html', context)
    