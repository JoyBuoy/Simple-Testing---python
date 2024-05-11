from hello import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 5) == 4
    assert add_numbers(0, 0) == 0
    assert add_numbers(10, -10) == 0
    assert add_numbers(100, 200) == 300