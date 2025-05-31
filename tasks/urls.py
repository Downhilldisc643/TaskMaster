from django.urls import path
from . import views

urlpatterns=[
    path('', views.task_list, name='task-list'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('update-status/<int:pk>/', views.update_status, name='update-status'),
]
