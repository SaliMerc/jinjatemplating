from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, "about.html")
def base (request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')