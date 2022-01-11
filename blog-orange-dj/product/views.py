from django.shortcuts import render

# Create your views here.
from .models import Category , Product
from django.core.paginator import Paginator
from django.db.models import Q

def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    #  todo search query
    search_query = request.GET.get('q')
    if search_query:
        products  = products.filter(
            Q(name__icontains = search_query)
        )

    # todo paginator
    paginator = Paginator(products , 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)


    context = {
        'categories':categories,
        'products': products,
    }
    return render(request , 'products.html' , context)



def product_by_category(request , category):
    product_by_category = Product.objects.filter(category__name=category)
    context = {

        'products': product_by_category,
    }


    return render(request , 'products.html' , context)