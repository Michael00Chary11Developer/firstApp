# from rest_framework.request import Request
# from rest_framework.response import Response
# from .models import Todo
# from .serializers import TodoSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view


# @api_view(['GET','POST'])
# def all_todos(request: Request):
#     if request.method == "GET":
#         todos = Todo.objects.order_by('priority').all()
#         todo_serializer = TodoSerializer(todos, many=True)
#         return Response(todo_serializer.data, status.HTTP_200_OK)
#     elif request.method == "POST":
#         deserialier = TodoSerializer(data=request.data)
#         if deserialier.is_valid():
#             deserialier.save()
#             return Response(deserialier.data, status.HTTP_201_CREATED)
#     return Response(None, status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


# POST And GRT

@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by("priority").all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serailizer = TodoSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_deatil_view(request: Request, todo_id=int):
    # if not exit error will occured => get error
    # todo = Todo.objects.get(pk=todo_id)
    # todo = Todo.objects.filter(pk=todo_id).first()
    try:
        todo = Todo.objects.get(pk=todo_id)
    except todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize = TodoSerializer(todo)
        return Response(serialize.data, status.HTTP_200_OK)
     
    # if request.method == "GET":
    #     serialize = TodoSerializer(todo)
    #     return Response(serialize.data, status.HTTP_200_OK)
