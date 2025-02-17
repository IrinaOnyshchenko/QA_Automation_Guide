import pytest
@pytest.mark.parametrize("number",[1,2,3])

def test_number_increase(number):
    assert (number+1)>number

@pytest.mark.parametrize("input, expected", [
    (1,2),
    (2,4),
    (3,6)
]
    )
def test_multiplication(input,expected):
    assert input*2 == expected