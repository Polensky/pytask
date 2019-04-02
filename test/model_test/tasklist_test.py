from helper import anyvalue

from pytask.model import Task, TaskList


def test_init():
    title_val, id_val = anyvalue(2)
    tasks = [Task(1, 1, 1), Task(2, 2, 2), ]

    task_list = TaskList(title_val, id_val, tasks)

    assert task_list.title == title_val
    assert task_list.id == id_val
    assert task_list.tasks == tasks


def test_pos():
    y_val, x_val = anyvalue(2)
    tasks = [Task(1, 1, 1), Task(2, 2, 2), ]

    task_list = TaskList('title', 'id', tasks)
    task_list.pos = y_val, x_val

    assert task_list.pos == (y_val, x_val)
    assert task_list.x == x_val
    assert task_list.y == y_val


def test_addstr():
    title_val, y_val, x_val = anyvalue(3)
    tasks = [Task(1, 1, 1), Task(2, 2, 2), ]

    task_list = TaskList(title_val, 'id', tasks)
    task_list.pos = y_val, x_val

    assert task_list.addstr() == (y_val, x_val, title_val)
