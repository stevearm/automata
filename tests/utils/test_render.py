import numpy

from   automata.utils import render

def test_scale_2d_array():
    field = numpy.array([
            [102,  3093,  46],
            [1020,   92, 846],
            [2102,   43, 662],
        ], dtype=numpy.int32)

    actual = render.scale_2d_array(field, 1000, 2000)
    expected = [
            [1019, 2000, 1000],
            [1320, 1016, 1263],
            [1675, 1000, 1202]]
    assert numpy.array_equal(actual, expected)

def test_scale_2d_array_with_given_bounds():
    field = numpy.array([
            [102,  3093,  46],
            [1020,   92, 846],
            [2102,   43, 662],
        ], dtype=numpy.int32)

    actual = render.scale_2d_array(field, 0, 100, 0, 10000)
    expected = [
            [ 1, 30, 0],
            [10,  0, 8],
            [21,  0, 6]]
    assert numpy.array_equal(actual, expected)
