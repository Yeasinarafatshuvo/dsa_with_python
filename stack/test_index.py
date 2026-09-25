import pytest
from index import Stack

def test_stack_is_empty_initially():
    stack = Stack()

    assert stack.is_empty() is True

def test_push():
    stack = Stack()
    stack.push(10)

    assert stack.items == [10]
    assert stack.is_empty() is False



def test_push_multiple_times():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.items == [10, 20, 30]


def test_pop():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    result = stack.pop()

    assert result == 20
    assert stack.items == [10]


def test_pop_follows_lifo():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10

def test_stack_empty_after_pop_all_items():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    stack.pop()
    stack.pop()

    assert stack.is_empty() is True


def test_stack_can_store_different_data_types():
    stack = Stack()

    stack.push(10)
    stack.push("hello")
    stack.push([1, 2, 3])

    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 10
    