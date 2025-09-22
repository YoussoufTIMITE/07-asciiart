import pytest
from main import artcode_i, artcode_r

def test_artcode_i_basic():
    assert artcode_i('MMMMaaacXolloMM') == [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    assert artcode_i('') == []
    assert artcode_i('A') == [('A', 1)]
    assert artcode_i('AAABBBCCDAA') == [('A', 3), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]

def test_artcode_r_basic():
    assert artcode_r('MMMMaaacXolloMM') == [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    assert artcode_r('') == []
    assert artcode_r('A') == [('A', 1)]
    assert artcode_r('AAABBBCCDAA') == [('A', 3), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]
