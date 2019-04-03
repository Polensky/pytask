from helper import anyvalue

from pytask.model import Displayable


def test_init_minimal():
    x_val, y_val, text_val = anyvalue(3)

    displayable = Displayable(x_val, y_val, text_val)

    assert displayable.x == x_val
    assert displayable.y == y_val
    assert displayable.text == text_val


def test_pos():
    y_val, x_val = anyvalue(2)

    displayable = Displayable(text='anything')
    displayable.pos = y_val, x_val

    assert displayable.pos == (y_val, x_val)
    assert displayable.x == x_val
    assert displayable.y == y_val


def test_addstr():
    text_val, y_val, x_val = anyvalue(3)

    displayable = Displayable(x_val, y_val, text_val)

    assert displayable.addstr() == (y_val, x_val, text_val)
