from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, JsonResponse, HttpResponse
# above is all component
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# hhtps

# Create your views here.


def index(request):
    context = {
        'alltodos': Todo.objects.order_by('priority').all()
    }
    return render(request, 'home/index.html', context)


# def todos_json(request: HttpRequest):
@api_view(['GET'])
def todos_json(request: Request):
    todos = list(Todo.objects.order_by(
        'priority').all().values('title', 'is_valid'))
    # return JsonResponse({"todo": todos})
    return Response({'todo': todos}, status.HTTP_200_OK)
