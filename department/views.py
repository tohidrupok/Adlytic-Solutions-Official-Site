from django.shortcuts import render, get_object_or_404
from .models import Category, Package , PackageOrder , Portfolio , TeamMember , Client
from .forms import PurchaseForm , ContactForm
import logging 
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):  
    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    package = Category.objects.filter(group__part="package")

    context = {'service': service, 'softwear': softwear, 'package': package}  

    return render(request, 'home2.html', context) 


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

    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package")

    
    
    package = get_object_or_404(Package, pk=id) 
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.package = package  #model aa package save
            order.save()
            context = {'form': form, 'success': True, 'id': id,'service': service, 'softwear': softwear, 'packages': packages} 

            return render(request, 'buy.html', context)
    else:
        form = PurchaseForm()

    context = {'package': package, 'form': form, 'success': False, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}
    return render(request, 'buy.html', context)
     

def about(request):
    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package")

    context = {'success': True, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}  

    return render(request,'about.html',context)

def portfolio(request):

    portfolio_items = Portfolio.objects.all()

    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package")

    context = {'portfolio_items': portfolio_items,'success': True, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}   

    
    return render(request, 'portfolio.html', context)


def team_member(request):

    team_members = TeamMember.objects.all()

    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package")

    context = {'team_members': team_members,'success': True, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}   

    
    return render(request, 'team.html', context)

def client(request):

    clients = Client.objects.all()

    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package")

    context = {'clients': clients,'success': True, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}   

    
    return render(request, 'client.html', context)



logger = logging.getLogger(__name__)
def my_contact(request):

    form = ContactForm()
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            
            # Send email to admin
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']  
            name = form.cleaned_data['name']
            admin_email = settings.DEFAULT_FROM_EMAIL  


            try:
                send_mail(
                    f"New contact form submission: {subject}",
                    f"Name: {name}\nEmail: {from_email}\n\nMessage:\n{message}",
                    admin_email,
                    [admin_email],
                    fail_silently=False,
                )
            except Exception as e:
                logger.error(f"Error sending email from {from_email} to {admin_email}: {e}")
                success = False
            
            form = ContactForm()  
    
    service = Category.objects.filter(group__part="service") 
    softwear = Category.objects.filter(group__part="softwear_solution")
    packages = Category.objects.filter(group__part="package") 
    

    context = {'success': success,'form': form, 'id': id,'service': service, 'softwear': softwear, 'packages': packages}   

    return render(request, 'contact.html', context) 
    

