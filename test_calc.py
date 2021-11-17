from calc import Calc

calc = Calc()
def test_mult_positive():
    x = 3
    y = 4
    res = 12
    assert calc.mult(x, y) == res, f"Проверка умножения не пройдена {x} * {y} != {res}"

def test_mult_negative():
    x = 3
    y = 4
    res = 10
    assert calc.mult(x, y) != res

def test_add_positive():
    x = 2
    y = 3
    res = 5
    assert calc.plus(x, y) == res, f"Проверка сложения не пройдена {x} + {y} != {res}"

