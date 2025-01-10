from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosViewSetView)

urlpatterns = [
    path('todos/', views.all_todos),
    path('todos/<int:todo_id>/', views.todo_deatil_view),
    path('cbv/', views.ListTodoView.as_view()),
    path('cbv/<int:todo_id>/', views.DetailView.as_view()),
    path('todos/mixins/', views.TodosListMixinApiView.as_view()),
    path('todos/mixins/<int:pk>', views.TodoDetailMixinApiView.as_view()),
    path('todos/generics/', views.TodoGenericApiView.as_view()),
    path('todos/generics/<int:pk>', views.TodoGenericDetailView.as_view()),
    path('todos/viewsets/', include(router.urls)),
    path('todos/users/', views.UserGenericApiView.as_view()),
    # path('cbv/',views.ManageTodoApiView.as_view()),
]
