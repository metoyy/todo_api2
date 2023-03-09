from django.urls import path

from . import views


urlpatterns = [
    # function urls
    path('tasks/', views.tasks_list),
    path('tasks/<int:pk>/', views.task_detail),
    path('tasks-create/', views.task_create),
    path('tasks-update/<int:pk>/', views.task_update),
    path('tasks-delete/<int:pk>/', views.task_delete),
]