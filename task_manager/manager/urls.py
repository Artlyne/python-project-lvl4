from django.urls import path
from task_manager.manager import views


urlpatterns = [
    path('', views.index),
]