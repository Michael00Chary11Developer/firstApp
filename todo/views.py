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
from .serializers import TodoSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema


# Create your views here.


# POST And GRT

# start classbaseview

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
def todo_deatil_view(request: Request, todo_id: int):
    # if not exit error will occured => get error
    # todo = Todo.objects.get(pk=todo_id)
    # todo = Todo.objects.filter(pk=todo_id).first()
    try:
        todo = Todo.objects.get(pk=todo_id)

    # must use class
    except Todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialize = TodoSerializer(todo)
        return Response(serialize.data, status.HTTP_200_OK)

    elif request.method == "PUT":
        serialize = TodoSerializer(todo, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        todo.delete()
        return Response(None, status.HTTP_400_BAD_REQUEST)

        # if request.method == "GET":
        #     serialize = TodoSerializer(todo)
        #     return Response(serialize.data, status.HTTP_200_OK)

# end classbaseview

# class ManageTodoApiView(APIView):
#     def get(self, request: Request):
#         todos = Todo.objects.order_by('priority').all()
#         todo_serialize = TodoSerializer(todos, many=True)
#         return Response(todo_serialize.data, status.HTTP_200_OK)

#     def post(self, request: Request):
#         deserialize = TodoSerializer(data=request.data)
#         if deserialize.is_valid():
#             deserialize.save()
#             return Response(deserialize.data, status.HTTP_201_CREATED)
#         else:
#             return Response(None, status.HTTP_400_BAD_REQUEST)


# class nase view

class ListTodoView(APIView):
    @extend_schema(
        request=TodoSerializer,
        responses={201: TodoSerializer},
        description="This is about todos!"
    )
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todos_serialize = TodoSerializer(todos, many=True)
        return Response(todos_serialize.data, status.HTTP_200_OK)

    def post(self, request: Request):
        deserialze = TodoSerializer(data=request.data)
        if deserialze.is_valid():
            deserialze.save()
            return Response(deserialze.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    def get_object(self, todo_id: int):
        # another way
        # todo = Todo.objects.filter(pk=todo_id).first()
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except Todo.DoesNotExist:
            return Response(None, status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id=todo_id)
        serialize = TodoSerializer(todo)
        return Response(serialize.data, status.HTTP_201_CREATED)

    def put(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id=todo_id)
        serialize = TodoSerializer(todo, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, reqeust: Request, todo_id: int):
        todo = self.get_object(todo_id=todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
# class nase view sonati


# region mixins

class TodosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset = Todo.objects.order_by("priority")
    # queryset.all()
    queryset = Todo.objects.order_by("priority").all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodoDetailMixinApiView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by("priority").all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

# end region mixins


# region generics  # very very very simple Code....

class TodoGenericPaginationView(PageNumberPagination):
    page_size = 2


class TodoGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = PageNumberPagination
    pagination_class = TodoGenericPaginationView
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TodoGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# end Generic region


# viewset region

class TodosViewSetView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by("priority").all()
    serializer_class = TodoSerializer

# end viewset region


# region users

User = get_user_model()


class UserGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# endregion
