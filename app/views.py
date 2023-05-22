from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import Product, Customer, Cart
from .forms import CustomerRegistrationForm, LoginForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())

class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer registration successfully!')
        else:
            messages.error(request, 'Invalid input data! Please try again.')
        return render(request, 'app/customerregistration.html', locals())

class LoginView(View):
    def get(self, request):
        form= LoginForm()
        return render(request, 'app/customerlogin.html', locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']


            reg = Customer(user=user, first_name=first_name, last_name=last_name, mobile=mobile, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Oppss! Something went wrong')
        return render(request, 'app/profile.html', locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())

class UpdateAddress(View):
    def get(self, request, pk, quaryset=None):
        add = Customer.objects.get(pk=pk)
        form= CustomerProfileForm(instance=add)
        return render(request, 'app/update_address.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.first_name = form.cleaned_data['first_name']
            add.last_name = form.cleaned_data['last_name']
            add.mobile = form.cleaned_data['mobile']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
        
            add.save()
            messages.success(request, 'Your Address updated successfully!')
        else:
            messages.error(request, 'Opss! Something went wrong!')

        return redirect('address')

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discount_price
        amount = amount + value
    totalamount = amount + 0 # add shipping price

    return render(request, 'app/addtocart.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
           value = p.quantity * p.product.discount_price
           amount += value
        totalamount = amount + 0 
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)