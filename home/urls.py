from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.todo_list, name="todo_list"),
    path("home/create_todo", views.create_todo, name="create_todo"),
    path('home/complete/<int:home_id>', views.complete_todo, name = "complete_todo"),
    path('home/delete/<int:home_id>', views.delete_todo, name = "delete_todo")
    
]
