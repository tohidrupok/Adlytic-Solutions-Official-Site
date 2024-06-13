from django.shortcuts import render, get_object_or_404
from .models import Category, Package , PackageOrder 
from .forms import PurchaseForm

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


def buy(request, id):
    package = get_object_or_404(Package, pk=id)
    print(package)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.package = package  #model aa package save
            order.save()
            return render(request, 'buy.html', {'form': form, 'success': True, 'id': id})
    else:
        form = PurchaseForm()

    return render(request, 'buy.html', {'form': form, 'success': False, 'id': id, 'package': package})
    