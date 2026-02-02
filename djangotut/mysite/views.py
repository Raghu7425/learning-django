from django.http import HttpResponse
from django.shortcuts import render

def about_page(request):
    return HttpResponse("Hello")
def d_page(request):
    return HttpResponse("<h1><center>Hello from page 2<center><h1>")
def index_page(request):
    return render(request, "index.html")