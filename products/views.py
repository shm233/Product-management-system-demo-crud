from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import *

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        user_exists = UserModel.objects.filter(username = username).exists()
        if user_exists:
            messages.warning(request, "You DARE to choose the name of the chosen??!!")
            return redirect('sign_up')
        
        if password == password2:
            UserModel.objects.create_user(
                username = username,
                full_name = full_name,
                email = email,
                password = password
            )
            messages.success(request, "It's a great honor for you to be here")
            return redirect('sign_in')
        else:
            messages.warning(request, "Are you blind?! Can't you match a small password?")
            return redirect('sign_up')
    return render(request, 'authenticate/sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_id = authenticate(request, username = username, password = password)
        if user_id:
            login(request, user_id)
            messages.success(request, "Embark on your journey")
            return redirect('home_view')
        else:
            messages.warning(request, "You DARE to come here unwelcomed?!")
            return redirect('sign_in')
    return render(request, 'authenticate/sign-in.html')

@login_required
def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required
def home_view(request):
    context = {
        'hello' : 'WELCOME',
    }
    return render(request, 'home.html', context)

@login_required
def product_list(request):
    products = ProductModel.objects.filter(created_by = request.user)
    context = {
        'pro' : products
    }
    return render(request, 'product-list.html', context)

@login_required
def add_product(request):
    current_user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product_image = request.FILES.get('product_image')
        production_date = request.POST.get('production_date')
        
        ProductModel.objects.create(
            name = name,
            description = description,
            price = price,
            product_image = product_image,
            production_date = production_date,
            created_by = current_user
        )
        messages.success(request, "Your New Product Entry has been added successfully")
        return redirect('product_list')
    return render(request, 'add-product.html')

@login_required
def update_product(request,p_id):
    products = ProductModel.objects.get(id = p_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product_image = request.FILES.get('product_image')
        production_date = request.POST.get('production_date')
        
        products.name = name
        products.description = description
        products.price = price
        if product_image:
            products.product_image = product_image
        products.production_date = production_date
        products.save()
        messages.success(request, "Information Orthodoxly Update")
        return redirect('product_list')
    context = {
        'pro' : products
    }
    return render(request, 'update-product.html', context)

@login_required
def delete_product(request, p_id):
    ProductModel.objects.get(id = p_id).delete()
    return redirect('product_list')
