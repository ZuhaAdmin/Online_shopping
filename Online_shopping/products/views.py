from django.shortcuts import render, get_object_or_404, redirect
from .models import Categories, Types, Tags, Colors, Products
from account.forms import Loginform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Products
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def products(request, category_slug=None, type_slug=None, tag_slug=None, color_slug=None):
    category = None
    type = None
    tag = None
    color = None
    categories = Categories.objects.all()
    types = Types.objects.all()
    tags = Tags.objects.all()
    colors = Colors.objects.all()[:12]
    products = Products.objects.filter(available=True)[:15]

    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        products = Products.objects.filter(category=category)

    if type_slug:
        type = get_object_or_404(Types, slug=type_slug)
        products = Products.objects.filter(type=type)

    if tag_slug:
        tag = get_object_or_404(Tags, slug=tag_slug)
        products = Products.objects.filter(tag=tag)

    if color_slug:
        color = get_object_or_404(Colors, slug=color_slug)
        products = Products.objects.filter(color=color)

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
        'category':category,
        'type':type,
        'tag':tag,
        'color':color,
        'categories':categories,
        'types':types,
        'tags':tags,
        'colors':colors,
        'products':products,
        'form_l':form_l
    }
    return render(request, template_name='product.html', context=data)

def product_detail(request, id, slug):
    categories = Categories.objects.all()
    types = Types.objects.all()
    tags = Tags.objects.all()
    colors = Colors.objects.all()[:12]
    products = Products.objects.all()[:15]

    data = {
        'categories':categories,
        'types':types,
        'tags':tags,
        'colors':colors,
        'products':products,    
    }
    return render(request, template_name='product-detail.html', context=data)

@login_required(login_url="/account")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("/product")


@login_required(login_url="/account")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account")
def cart_detail(request):
    return render(request, 'cart.html')

def cart(request):
    categories = Categories.objects.all()
    types = Types.objects.all()

    data = {
        'categories':categories,
        'types':types,
    }
    return render(request, template_name='cart.html', context=data)

def checkout(request):
    categories = Categories.objects.all()
    types = Types.objects.all()

    data = {
        'categories':categories,
        'types':types,
    }
    return render(request, template_name='checkout.html', context=data)

def wishlist(request):
    categories = Categories.objects.all()
    types = Types.objects.all()

    data = {
        'categories':categories,
        'types':types,
    }
    return render(request, template_name='wishlist.html', context=data)