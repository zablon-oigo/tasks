from django.urls import path
from .views import (create_task, home,detail_task,delete_task, update_task, list_task,task_complete)


urlpatterns=[
    path('',home, name='home'),
    path('list/', list_task, name='list'),
    path('detail/<int:id>/<slug:slug>/', detail_task, name='detail'),
    path('create/', create_task, name='create'),
    path('update/<int:id>/', update_task, name='update'),
    path('delete/<int:id>/',delete_task, name='delete'),
    path('<int:pk>/',task_complete,name='task_complete'),
]