from bootstrap_modal_forms.forms import BSModalForm
from modalform.models import TodoItem


class CreateUpdateTodoItemForm(BSModalForm):
    class Meta:
        model = TodoItem
        fields = ['item', 'item_date']

