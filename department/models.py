from django.db import models 

class Name(models.Model):
    part = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.part
    
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='category_images/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Name, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.category_name} ({self.group.part})"


class Package(models.Model):
    category = models.ManyToManyField(Category, related_name='packages')
    package_name = models.CharField(max_length=100, null=True, blank=True)
    functions = models.TextField(null=True, blank=True) 
    amount = models.CharField(max_length=10)
    calling_software = models.TextField(null=True, blank=True)
    crm = models.TextField(null=True, blank=True)
    ticket_software = models.TextField(null=True, blank=True)
    user_administration = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        categories_list = ', '.join(category.category_name for category in self.category.all())
        return f"{self.package_name} (Categories: {categories_list})"