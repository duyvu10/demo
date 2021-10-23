from calc import add


def test_add(x, y):
    if(add(x, y) == x+y):
        return True
    else:
        return False


test_add(1, 1)
