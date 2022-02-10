from urllib import request
from django.shortcuts import render, redirect
from products.models import Categories, Types, Tags, Colors, Products
from account.forms import Loginform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def mainpage(request):
    categories = Categories.objects.all()
    types = Types.objects.all()
    products = Products.objects.all()[:4]
    maincategories = Categories.objects.all()

    form_l = Loginform()
    if request.method == "POST":
        form_l = AuthenticationForm(request, request.POST)

        if form_l.is_valid():
            username = form_l.cleaned_data.get('username')
            password = form_l.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    data = {
        'categories':categories,
        'types':types,
        'products':products,
        'form_l':form_l,
        'maincategories':maincategories,
    }
    return render(request, template_name='index.html', context=data)
