from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<a href='/'> < Back</a> Blogs Page")
    return render(request, 'blog/index.html')