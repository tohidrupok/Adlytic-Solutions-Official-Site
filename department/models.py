from django.db import models 

class Name(models.Model):
    part = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.part
    
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='media/category_images/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Name, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.category_name} ({self.group.part})"


class Package(models.Model):
    category = models.ManyToManyField(Category, related_name='packages')
    package_name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    functions = models.SlugField(max_length=200, unique=True , null=True, blank=True) 
    amount = models.CharField(max_length=20)
    calling_software = models.CharField(max_length=500, null=True, blank=True)
    crm = models.CharField(max_length=1300, null=True, blank=True)
    ticket_software = models.CharField(max_length=500, null=True, blank=True)
    user_administration = models.CharField(max_length=1300, null=True, blank=True)
    
    
    def __str__(self):
        categories_list = ', '.join(category.category_name for category in self.category.all())
        return f"{self.package_name} (Categories: {categories_list})"         
    

class PackageOrder(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        if self.package:
            return f"{self.name} ordered {self.package.package_name}"
        else:
            return f"{self.name} ordered an unspecified package"

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/portfolio_images/', null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title 
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Team_member/', null=True, blank=True)

    def __str__(self):
        return self.name 

class Client(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='Client/', null=True, blank=True)
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name  


class Service(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name  

