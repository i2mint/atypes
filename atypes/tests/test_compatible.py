import pytest
from typing import List, Dict, Union, Tuple
from collections.abc import Callable, Iterable
from atypes.compatible import has_compatible_type, builtins


def test_builtins_leaves():

    assert has_compatible_type(int, float)
    assert has_compatible_type(int, int)
    assert has_compatible_type(list[int], list[float])


def test_unions():
    t1 = Union[int, float]
    t2 = Union[str, bool]
    t3 = Union[float, str]
    assert has_compatible_type(t1, t3)
    assert not has_compatible_type(t1, t2)


def test_list():
    assert has_compatible_type(list[int], list[float])
    assert not has_compatible_type(list[float], list[int])


def test_dict():
    assert has_compatible_type(dict[str, list[int]], dict[str, list[float]])


def test_classes():
    class A:
        pass

    class B(A):
        pass

    assert has_compatible_type(A, B)


def test_tuple():
    t1 = tuple[int, float]
    t2 = tuple[float, float]
    assert has_compatible_type(t1, t2)


def test_callable():
    assert has_compatible_type(
        Callable[[float, float], int], Callable[[int, float], int]
    )
    # assert not has_compatible_type(List[float], List[int])
