"""Online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainpage.views import mainpage
from products.views import products, product_detail, cart, checkout, wishlist
from products import views
from account.views import acoountpage, logoutpage, activate
from contact.views import contact, notfound
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage, name='mainpg'),
    path('productdetail/', product_detail, name='productdetail'),
    path('account/', acoountpage, name='accountpg'),
    path('logout/', logoutpage, name='logout'),
    path('product/', products, name='products'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('contact/', contact, name='contact'),
    path('notfound/', notfound, name='notfound'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('tags/<slug:tag_slug>/', products, name='product_list_by_tags'),
    path('categories/<slug:category_slug>/', products, name='product_list_by_category'),
    path('types/<slug:type_slug>/', products, name='product_list_by_types'),
    path('colors/<slug:color_slug>/', products, name='product_list_by_colors'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
