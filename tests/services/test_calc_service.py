import pytest
from services import calc_service


@pytest.mark.service
def test_add1():

    number = 1
    assert calc_service.add1(number) == 2


@pytest.mark.service
def test_add2():

    number = 2
    for i in range(0, 10000):
        print(i)
    assert calc_service.add1(number) == 3


@pytest.mark.service
def test_add3():

    number = 2
    for i in range(0, 10000):
        print(i)
    assert calc_service.add1(number) == 3
