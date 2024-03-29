from todo_app.data.todo_item import Item


class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        all_items = self._items

        output = []

        for item in all_items:
            if item.status == "To Do":
                output.append(item)

        return output
    
    @property
    def done_items(self):
        all_items = self._items

        output = []

        for item in all_items:
            if item.status == "Done":
                output.append(item)

        return output
    