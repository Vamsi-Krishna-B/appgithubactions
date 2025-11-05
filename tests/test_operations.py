from src.mathoperations import add,sub 
def test_add():
    assert add(2,3) == 5
    assert add(3,4) ==7
    assert add(-13,52) == 39

def test_sub():
    assert sub(2,3) == -1
    assert sub(34,3) == 31
    assert sub(23,-3) == 26