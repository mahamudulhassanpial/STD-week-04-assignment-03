from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_Post, name='add_Post'),
    path('edit/<int:id>', views.edit_Post, name='edit_Post'),
    path('delete/<int:id>', views.delete_Post, name='delete_Post'),
     path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('show/', views.show_tasks, name='show_tasks'),
]