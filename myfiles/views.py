import random

from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(requests):
    ctg = Kategoriyalar.objects.all()
    advertising = Advertising.objects.all()
    sneaker = Krosofkalar.objects.all()
    random_sneak = random.choice(advertising)
    ctx = {
        'ctg':ctg,
        'sneaker': sneaker,
        'random_sneak': random_sneak,
    }
    return render(requests, 'blog/index.html', ctx)

def contact(requests):
    ctx = {}
    return render(requests, 'blog/contact.html', ctx)


def products(requests, slug=None):
    ctg = Kategoriyalar.objects.all()
    category = Kategoriyalar.objects.get(slug=slug)
    sneaker = Krosofkalar.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg':ctg,
        'category':category,
        'sneaker':sneaker
    }
    return render(requests, 'blog/products.html', ctx)


def register(requests):
    ctx = {}
    return render(requests, 'blog/register.html', ctx)

def single(requests, pk=None):
    ctg = Kategoriyalar.objects.all()
    sneakers = Krosofkalar.objects.all()
    random_s = random.choices(sneakers, k=3)
    products_pk = Krosofkalar.objects.get(pk=pk)
    form = ChoiceForm()
    if requests.POST:
        forms = ChoiceForm(requests.POST or None, requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Sotib_olinganlar.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg':ctg,
        'product_pk':products_pk,
        'form':form,
        'random_s': random_s,
        'sneakers': sneakers,
    }
    return render(requests, 'blog/single.html', ctx)