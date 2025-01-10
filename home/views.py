from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import CreateForm


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def sayhello(request):
    # return HttpResponse("hello user")
    # person = {"name": "michael"}
    # return render(request, 'index.html',context=person)
    # return render(request, 'index.html', context={"name": "michael"})
    return render(request, 'index.html', context={"name": "admin"})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successful!!!!!', 'success!')
    return redirect('home')


def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'],
                                body=cd['body'], create=cd['create'])
            messages.success(request, 'Todo created success!', "success")
            return redirect('home')
        #home=>namespace => home:home
    else:
        form = CreateForm()

    return render(request, 'create.html', {'form': form})
