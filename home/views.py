from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    peoples = [
        {'Name':'Asad', 'Age':23},
        {'Name':'Ali', 'Age':18},
        {'Name':'Adnan', 'Age':24},
        {'Name':'Mohsin', 'Age':17},
        {'Name':'Waqas', 'Age':16}
    ]
    return render(request, "home/index.html", context={'peoples': peoples, 'page':'Django Tutorial'})

def about(request):
    context = {'page':'about'}
    return render(request, "home/about.html", context) 

def contact(request):
    context = {'page':'contact'}
    return render(request, "home/contact.html", context)