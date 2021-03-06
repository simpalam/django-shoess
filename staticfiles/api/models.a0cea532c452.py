from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group

from .managers import UserManager,GroupManager
from django.conf import settings

TYPE=(('men','Men'),
('women','Women'),
('kids','Kids'))


STATUS=(('new','New'),
('sale','Sale'),
('feature','Feature'))

COLOR=((''))



class User(AbstractBaseUser,PermissionsMixin):
    """
    Custom abstract user Model.
    """
    # Names
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    # contact
    email = models.EmailField(unique=True)  # require
  
    # avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Permission
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
  
    # Main Field for authentication
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = "email" 
    # When user create must need to fill this field
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
    class Meta:
        ordering = ('-created_at', '-updated_at', )

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name}  {self.last_name}'
        return self.email.split('@')[0]

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
   

# Create your models here.
class Size(models.Model):
    title=models.CharField(max_length=30,null=True)
    value=models.IntegerField()

    def __str__(self):
        return self.title

class Color(models.Model):
    title=models.CharField(max_length=50)
    value=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title=models.CharField(max_length=50)
    url=models.ImageField(upload_to='gallery')
    color=models.ManyToManyField(Color)

    def __str__(self):
        return self.title


class Product(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    type=models.CharField(max_length=50,choices=TYPE)
    status=models.CharField(max_length=50,choices=STATUS,null=True)
    color=models.ManyToManyField(Color)
    size=models.ManyToManyField(Size,null=True)
    unit=models.IntegerField(blank=True,null=True)
    price=models.IntegerField()
    salePrice=models.IntegerField()
    discountInPercent=models.IntegerField(blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='product')
    gallery=models.ManyToManyField(Gallery)

    def __str__(self):
        return self.name


class Children(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    type=models.CharField(max_length=50,choices=TYPE)
    products=models.ManyToManyField(Product)

    def __str__(self):
        return self.title

    
class Category(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    type=models.CharField(max_length=50,choices=TYPE)
    # children=models.ManyToManyField(Children,null=True)
    products=models.ManyToManyField(Product)

    def __str__(self):
        return self.title
