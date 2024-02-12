from todo_app.data.todo_item import Item
from todo_app.viewmodel import ViewModel


def test_view_model_done_property_only_returns_done_todos_and_nothing_else():
    # Arrange
    items = [
        Item(1, "Visit the shop", "To Do"),
        Item(2, "Go to the Cinema", "Done")
    ]
    view_model = ViewModel(items)

    # Act
    returned_items = view_model.done_items

    # Assert
    assert len(returned_items) == 1
    single_item = returned_items[0]
    assert single_item.status == "Done"
