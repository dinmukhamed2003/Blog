from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from product.models import Product, Category, Review
from product.forms import ProductCreateForms, ReviewCreateForm



# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def now_time_view(request):
    if request.method == "GET":
        date = datetime.now()
        return HttpResponse(f"{date}")

def goodbye_view(request):
    if request.method == "GET":
        return HttpResponse('Goodbye user !')

def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context_data = {
            'products': products
        }
        return render(request, 'products/products.html', context=context_data)

def category_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        context_data = {
            'categories': categories
        }
        return render(request, 'categories/categories.html', context=context_data)

def detail_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        reviews = Review.objects.filter(product=product)

        data = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm,
        }

        return render(request, 'products/detail.html', context=data)
    if request.method == 'POST':
        form = ReviewCreateForm(data=request.data)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=kwargs['id']
            )
            return redirect(f"/product/{kwargs['id']}/")



def products_create_view(request):
    if request.method == 'GET':
        data = {
            'form': ProductCreateForms,

        }
        return render(request, 'products/create.html', context=data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForms(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/product')

        return render(request, 'product/create.html', context={
            'form': form
        })
