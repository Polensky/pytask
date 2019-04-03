from helper import anyvalue

from pytask.model import Tasklist


def test_init():
    title_val, id_val = anyvalue(2)

    tasklist = Tasklist(title_val, id_val)

    assert tasklist.title == title_val
    assert tasklist.id == id_val


def test_pos():
    y_val, x_val = anyvalue(2)

    tasklist = Tasklist('title', 'id')
    tasklist.pos = y_val, x_val

    assert tasklist.pos == (y_val, x_val)
    assert tasklist.x == x_val
    assert tasklist.y == y_val


def test_addstr():
    title_val, y_val, x_val = anyvalue(3)

    tasklist = Tasklist(title_val, 'id')
    tasklist.pos = y_val, x_val

    assert tasklist.addstr() == (y_val, x_val, title_val)
