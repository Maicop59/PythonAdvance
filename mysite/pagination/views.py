from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.core.cache.backends.base import InvalidCacheBackendError
# from django.core import cache

# Create your views here.
@cache_page(60*15)
def listing(request):
    try:
        customer_list = caches['customer_list']
        print(f'getdataformcache{customer_list}')
    except InvalidCacheBackendError :
        customer_list = Customer.objects.all()
        caches['customer_list'] = customer_list
        print(f"getdatabase{customer_list}")

    paginator = Paginator(customer_list,5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'pagination_1.html', {'customers':customers})




def listing_2(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list,5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'pagination_2.html', {'customers':customers})

def listing_addbase1(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list,5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'pagination_addbase.html', {'customers':customers})

def listing_addbase_ver2(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list,5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'pagination_addbase_ver2.html', {'customers':customers})