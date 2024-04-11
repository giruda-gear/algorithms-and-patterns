from pytest import raises
from solutions.dynamic_array import DynamicArray


def test_dynamic_array():
    dynamic_array = DynamicArray()

    dynamic_array.pushback(1)

    assert dynamic_array.getSize() == 1
    assert dynamic_array.getCapacity() == 10
    assert dynamic_array.get(0) == 1

    dynamic_array.set(0, 5)
    dynamic_array.get(0) == 5

    dynamic_array.pushback(10)
    assert dynamic_array.popback() == 10
    assert dynamic_array.getSize() == 1

    with raises(IndexError):
        dynamic_array.get(20)
