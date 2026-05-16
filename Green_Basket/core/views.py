from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Vendor
from django.contrib.auth.decorators import login_required

# 1. Home Page: List all products
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/home.html', {'products': products, 'categories': categories})

# 2. Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

# 3. Vendor Dashboard: Where farmers see their products
@login_required
def vendor_dashboard(request):
    if not request.user.is_vendor:
        return redirect('home')
    
    vendor = Vendor.objects.get(user=request.user)
    my_products = Product.objects.filter(vendor=vendor)
    return render(request, 'core/dashboard.html', {'products': my_products, 'vendor': vendor})

# 4. Add Product (For Vendors)
@login_required
def add_product(request):
    if request.method == 'POST':
        # Simplified logic: in real app, use Django Forms
        vendor = Vendor.objects.get(user=request.user)
        Product.objects.create(
            vendor=vendor,
            name=request.POST['name'],
            price=request.POST['price'],
            category_id=request.POST['category'],
            description=request.POST['description'],
            stock=request.POST['stock'],
            image=request.FILES['image']
        )
        return redirect('vendor_dashboard')
    
    categories = Category.objects.all()
    return render(request, 'core/add_product.html', {'categories': categories})