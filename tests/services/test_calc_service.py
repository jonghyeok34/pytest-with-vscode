import pytest
from app.services import calc_service


@pytest.mark.service
def test_add1():

    number = 1
    assert calc_service.add1(number) == 2


@pytest.mark.service
def test_add2():

    number = 2
    assert calc_service.add1(number) == 3