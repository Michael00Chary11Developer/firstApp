from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.sayhello),
    path('', views.home)
]
