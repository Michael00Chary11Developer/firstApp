from django.shortcuts import render
# from django.http import HttpResponse
from .models import Todo


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def sayhello(request):
    # return HttpResponse("hello user")
    # person = {"name": "michael"}
    # return render(request, 'index.html',context=person)
    # return render(request, 'index.html', context={"name": "michael"})
    return render(request, 'index.html', context={"name": "admin"})
