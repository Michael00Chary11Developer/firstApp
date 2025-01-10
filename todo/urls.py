from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.all_todos),
    path('todos/<int:todo_id>/', views.todo_deatil_view)
]
