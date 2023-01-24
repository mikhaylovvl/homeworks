from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    if request.GET.get('sort'):
        if request.GET.get('sort') == 'name':
            catalog = Phone.objects.all().order_by('name')
        elif request.GET.get('sort') == 'min_price':
            catalog = Phone.objects.all().order_by('price')
        elif request.GET.get('sort') == 'max_price':
            catalog = Phone.objects.all().order_by('-price')
    else:
        catalog = Phone.objects.all()

    context = {
        'phones': catalog
    }
    return render(request, template, context)


def show_catalog_sorted(request):
    template = 'catalog.html'
    param = request.GET.get['sort']

    if param == 'name':
        catalog = Phone.objects.all().order_by('name')
    context = {
        'phones': catalog
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
