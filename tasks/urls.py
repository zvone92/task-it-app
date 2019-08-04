from django.urls import path
from . import views


urlpatterns = [
    path('add', views.add, name='add'),
    path('<int:task_id>', views.detail, name='detail'),
    path('<int:task_id>/edit', views.edit, name='edit'),
    path('<int:task_id>/task_done', views.task_done, name='task_done'),


]
