from django.shortcuts import render, HttpResponse
from datetime import datetime
from product.models import Product

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

