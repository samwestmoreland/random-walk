import pytest
from sticky import force, calculate_new

def test_force():
    dims = 300

    result = force(150, dims)
    expected = 0
    assert result == expected

    result = force(50, dims)
    expected = -1/10000
    assert result == expected

def test_calculate_new():
    dims = 100
    m = dict()
    for i in range(5000):
        new = calculate_new(48, dims)
        if new in m:
            m[new] += 1
        else:
            m[new] = 1

    max_freq = 0
    result = 0
    for i in m:
        if m[i] > max_freq:
            result = i
            max_freq = m[i]

    assert result == 49

