from urllib import request
from django.shortcuts import render
from products.models import Categories,Types
# Create your views here.
def contact(request):
    categories = Categories.objects.all()
    types = Types.objects.all()

    data = {
        'categories':categories,
        'types':types,
    }
    return render(request, template_name='contact.html', context=data)

def notfound(request):
    categories = Categories.objects.all()
    types = Types.objects.all()

    data = {
        'categories':categories,
        'types':types,
    }
    return render(request, template_name='404.html', context=data)