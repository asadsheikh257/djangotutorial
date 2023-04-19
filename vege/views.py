from django.shortcuts import render
from .models import *

# Create your views here.

# def receipes(request):
#     return render(request, "receipe/receipes.html")


def receipes(request):
    context = {'page':'recepie'}
    if (request.method == "POST"):  
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        # print(receipe_name)
        # print(receipe_description)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )



    return render(request, "receipe/receipes.html", context) 