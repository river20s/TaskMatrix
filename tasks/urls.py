from django.urls import path
from .views import home, task_list, task_create, task_update, task_delete, task_list_create, task_list_update, task_list_delete, update_task_category

urlpatterns = [
    path('', home, name='home'),
    path('list/add/', task_list_create, name='task_list_create'),
    path('list/edit/<int:pk>/', task_list_update, name='task_list_update'),
    path('list/delete/<int:pk>/', task_list_delete, name='task_list_delete'),
    path('list/<int:pk>/', task_list, name='task_list'),
    path('list/<int:pk>/add/', task_create, name='task_create'),
    path('edit/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('update/<int:pk>/<int:category>/', update_task_category, name='update_task_category'),
]
