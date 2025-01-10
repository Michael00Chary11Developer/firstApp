from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('test/', views.todos_json, name="test")
]
