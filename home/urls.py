from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.sayhello, name='hi'),
    path('', views.home, name='home'),
    path('detail/<int:todo_id>/', views.detail, name='detail'),
    # path('detail/<int:todo_id>/', views.detail)
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('create', views.create, name='create')
]
