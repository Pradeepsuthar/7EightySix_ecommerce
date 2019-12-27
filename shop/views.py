from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
# Done : Start index function
def index(request):
    # Display all category products
    products = Product.objects.all()
    n = len(products)
    nproducts = n//4 + ceil((n/4)-(n//4))
    params = {'product' : products,'no_of_products':nproducts,'range':range(nproducts)}
    return render(request, 'shop/index.html',params)
# Done : End index function

def aboutUs(request):
    # return HttpResponse("<a href='/'> < Back</a> About Us")
    return render(request, 'shop/about.html')

def contactUs(request):
    # return HttpResponse("<a href='/'> < Back</a> Contact Us")
    return render(request, 'shop/contact.html')

def tracking(request):
    return HttpResponse("<a href='/'> < Back</a> Track order")
    # return render(request, 'shop/track_order.html')

def searching(request):
    return HttpResponse("<a href='/'> < Back</a> Search")
    # return render(request, 'shop/search.html')

def checkoutPage(request):
    return HttpResponse("<a href='/'> < Back</a> checkout")
    # return render(request, 'shop/checkout.html')

def viewProduct(request,id):
    # fetch products by id
    product = Product.objects.filter(id=id)

    return render(request, 'shop/products.html',{'product': product[0]})

def addtoCart(request):
    # return HttpResponse("<a href='/'> < Back</a> Cart")
    return render(request, 'shop/shopingCart.html')

def forMenCategory(request):
    allmenProducts = []
    allMainCategory = Product.objects.values('main_product_category','id')
    main_category = {cat_item['main_product_category'] for cat_item in allMainCategory }
    for main_category_product in main_category:
        print("\n\nMain Category :",main_category_product)
        if main_category_product == 'Men':
            products = Product.objects.filter(main_product_category=main_category_product)
            print("\n\nMy Products :",products)
            n = len(products)
            nproducts = n//4 + ceil((n/4)-(n//4))
            allmenProducts.append([products,range(1,nproducts),nproducts])
            print("\n\nAll Products :",allmenProducts)
    params = {'allmenproducts':allmenProducts}
    return render(request, 'shop/men.html',params)

def forWoMenCategory(request):
    allwomenProducts = []
    allMainCategory = Product.objects.values('main_product_category','id')
    main_category = {cat_item['main_product_category'] for cat_item in allMainCategory }
    for main_category_product in main_category:
        print("\n\nMain Category :",main_category_product)
        if main_category_product == 'Women':
            products = Product.objects.filter(main_product_category=main_category_product)
            print("\n\nMy Products :",products)
            n = len(products)
            nproducts = n//4 + ceil((n/4)-(n//4))
            allwomenProducts.append([products,range(1,nproducts),nproducts])
            print("\n\nAll Products :",allwomenProducts)   
    params = {'allwomenproducts':allwomenProducts}
    return render(request, 'shop/women.html',params)

def forKidsCategory(request):
    allkidsProducts = []
    allMainCategory = Product.objects.values('main_product_category','id')
    main_category = {cat_item['main_product_category'] for cat_item in allMainCategory }
    for main_category_product in main_category:
        print("\n\nMain Category :",main_category_product)
        if main_category_product == 'Kids':
            products = Product.objects.filter(main_product_category=main_category_product)
            print("\n\nMy Products :",products)
            n = len(products)
            nproducts = n//4 + ceil((n/4)-(n//4))
            allkidsProducts.append([products,range(1,nproducts),nproducts])
            print("\n\nAll Products :",allkidsProducts) 
    params = {'allkidsproducts':allkidsProducts}
    return render(request, 'shop/kids.html',params)