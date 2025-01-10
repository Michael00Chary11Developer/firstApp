from django.shortcuts import render
from .models import Title
from .serializers import TitleSerializer
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class ViewSetExample(viewsets.ModelViewSet):
    queryset = Title.objects.order_by("id").all()
    serializer_class = TitleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DetailMixinsExample(DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Title.objects.order_by("id").all()
    serializer_class = TitleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)


class MixinsExample(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Title.objects.order_by("id").all()
    serializer_class = TitleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class GenericExample(CreateAPIView, ListAPIView):
    queryset = Title.objects.order_by("id").all()
    serializer_class = TitleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DetailGenericExample(DestroyAPIView, RetrieveAPIView, UpdateAPIView):
    queryset = Title.objects.order_by("id").all()
    serializer_class = TitleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
