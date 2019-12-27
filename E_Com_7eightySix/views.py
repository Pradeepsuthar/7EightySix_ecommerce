from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("7EightySix Home Page")
    # return render(request, 'homeSite/index.html')