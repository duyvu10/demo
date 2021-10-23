import calc as ca


def test_add(x, y):
    if(ca.add(x, y) == x+y):
        return True
    else:
        return False


test_add(1, 1)
