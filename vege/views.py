from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# def receipes(request):
#     return render(request, "receipe/receipes.html")


def receipes(request):
    context = {'page':'Add-Recepie'}
    if (request.method == "POST"):  
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/receipes/')



    return render(request, "receipe/receipes.html", context) 

def show_receipe(request):
    # context = {'page':'Receipe'}
    queryset = Receipe.objects.all() 

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes': queryset, 'page':'Receipe'}
    return render(request, 'receipe/show_receipe.html', context)

def delete_receipe(request, id):
    queryset =  Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/show_receipe/')

def update_receipe(request, id): 
    queryset = Receipe.objects.get(id = id)
    if (request.method == "POST"):
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image :
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/show_receipe/')

    context = {'receipe':queryset}

    return render(request, 'receipe/update_receipe.html', context)




def login(request):
    context = {'page':"Login"}
    return render(request, 'receipe/login.html', context)

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('passowrd')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken.")
            return redirect('/register/')
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account registered successfully")

        return redirect('/register/')


    context = {'page':"Registation"}
    return render(request, 'receipe/register.html', context)