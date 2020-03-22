from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from modalform.forms import CreateUpdateTodoItemForm
from modalform.models import TodoItem


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def show_todo_items(request):
    all_items = TodoItem.objects.filter(user=request.user)
    return render(request, 'show_todo_items.html', {'all_items': all_items})


class CreateTodoItemFormView(BSModalCreateView):
    template_name = 'creat_modal_form.html'
    form_class = CreateUpdateTodoItemForm
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('show_todo_items')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(CreateTodoItemFormView, self).form_valid(form)


class UpdateTodoItemFormView(BSModalUpdateView):
    model = TodoItem
    template_name = 'update_modal_form.html'
    form_class = CreateUpdateTodoItemForm
    success_message = 'Success: Item was updated.'
    success_url = reverse_lazy('show_todo_items')


def delete_todo_item(request, todo_id):
    item = TodoItem.objects.get(pk=todo_id)
    item.delete()
    messages.success(request, ('Deleted successfully!'))
    return redirect('show_todo_items')
