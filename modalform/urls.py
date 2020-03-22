from django.urls import path
from modalform import views

urlpatterns = [
    path('', views.show_todo_items, name='show_todo_items'),
    path('create_todo_item/', views.CreateTodoItemFormView.as_view(), name='create_todo_item'),
    path('update_todo_item/<int:pk>', views.UpdateTodoItemFormView.as_view(), name='update_todo_item'),
    path('delete_todo_item/<todo_id>', views.delete_todo_item, name='delete_todo_item'),
]
