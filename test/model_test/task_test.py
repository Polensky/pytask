import random
import string
import pytest

from pytask.model import Task


def anyvalue(N=1, size=8):
    return [''.join(random.choices(string.ascii_uppercase + string.digits, k=size)) for _ in range(N)]


def test_init_minimal():
    title_val, id_val, status_val = anyvalue(3)

    task = Task(title_val, id_val, status_val)

    assert task.title == title_val
    assert task.id == id_val
    assert task.status == status_val
    assert task.position is None
    assert task.completed is None
    assert task.updated is None
    assert task.x == 0
    assert task.y == 0


def test_init_full():
    title_val, id_val, status_val, position_val, completed_val, updated_val = anyvalue(6)

    task = Task(title_val, id_val, status_val, position=position_val, completed=completed_val, updated=updated_val)

    assert task.title == title_val
    assert task.id == id_val
    assert task.status == status_val
    assert task.position == position_val
    assert task.completed == completed_val
    assert task.updated == updated_val
    assert task.x == 0
    assert task.y == 0


def test_pos():
    y_val, x_val = anyvalue(2)

    task = Task('title', 'id', 'status')
    task.pos = y_val, x_val

    assert task.pos == (y_val, x_val)
    assert task.x == x_val
    assert task.y == y_val


def test_addstr():
    title_val, y_val, x_val = anyvalue(3)

    task = Task(title_val, 'id', 'status')
    task.pos = y_val, x_val
    assert task.addstr() == (y_val, x_val, title_val)


def test_from_dict():
    title_val, id_val, status_val, position_val, completed_val, updated_val, other_val = anyvalue(7)

    d = {
         "title": title_val,
         "id": id_val,
         "status": status_val,
         "position": position_val,
         "completed": completed_val,
         "updated": updated_val,
         "other": other_val,
    }
    task = Task.from_dict(d)

    assert task.title == title_val
    assert task.id == id_val
    assert task.status == status_val
    assert task.position == position_val
    assert task.completed == completed_val
    assert task.updated == updated_val
    assert task.x == 0
    assert task.y == 0

    with pytest.raises(AttributeError) as excinfo:
        task.other
    assert 'object has no attribute' in str(excinfo.value)
