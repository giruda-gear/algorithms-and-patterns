import pytest

from solutions.singly_linked_list import LinkedList


@pytest.fixture
def empty_linked_list():
    return LinkedList()


@pytest.fixture
def filled_linked_list():
    linked_list = LinkedList()
    for i in range(1, 6):
        linked_list.insertTail(i)
    return linked_list


def test_insert_head(empty_linked_list):
    empty_linked_list.insertHead(1)
    assert empty_linked_list.getValues() == [1]


def test_insert_tail(empty_linked_list):
    empty_linked_list.insertTail(1)
    assert empty_linked_list.getValues() == [1]


def test_get(filled_linked_list):
    assert filled_linked_list.get(5)  # index out of bound
    assert filled_linked_list.get(0) == 1
    assert filled_linked_list.get(2) == 3


def test_remove(filled_linked_list):
    assert filled_linked_list.remove(2) == True
    assert filled_linked_list.getValues() == [1, 2, 4, 5]
    assert filled_linked_list.remove(0) == True
    assert filled_linked_list.getValues() == [2, 4, 5]
    assert filled_linked_list.remove(10) == False 