from calculator import addition, subtraction, division



def test_addition():
    assert addition(1, 2) == 3
    
def test_substraction():
    assert subtraction(2, 1) == 1
    
def test_division():
    assert division(2,2) == 1