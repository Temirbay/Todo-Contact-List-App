from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.index, name="index"),
    path('todos/', views.todo_list, name="todo_list"),
    path('todos/<int:todo_id>', views.todo_detail, name="todo_detail"),
    path('todos/add', views.todo_add, name="todo_add"),
    path('todos/complete/<int:todo_id>', views.todo_complete, name="todo_complete"),
    path('todos/delete/<int:todo_id>', views.todo_delete, name="todo_delete"),
    path('todos/update/<int:todo_id>', views.todo_update, name="todo_update"),
    path('todos/sort/<int:sort_id>', views.todo_sort, name="todo_sort"),


    path('contacts', views.contact_list, name="contact_list"),
    path('contacts/<int:contact_id>', views.contact_detail, name="contact_detail"),
    path('contacts/add', views.contact_add, name="contact_add"),
    path('contacts/delete/<int:contact_id>', views.contact_delete, name="contact_delete"),
    path('contacts/sort/<int:sort_id>', views.contact_sort, name="contact_sort"),
]
