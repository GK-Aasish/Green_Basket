from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Custom User to handle roles
class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, blank=True)

# 2. Vendor Profile (The Farmer)
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    farm_name = models.CharField(max_length=255)
    district = models.CharField(max_length=100) # e.g., Kathmandu, Jhapa
    address = models.TextField()
    is_approved = models.BooleanField(default=False) # Admin must approve farmers

    def __str__(self):
        return self.farm_name

# 3. Product Categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# 4. The Agricultural Product
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default="kg") # kg, quintal, piece
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.vendor.farm_name}"