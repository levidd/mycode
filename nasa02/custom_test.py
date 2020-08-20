#!/usr/bin/env python3

import custom
import pytest

# from nasa02 import custom

@pytest.mark.parametrize("test_input, expected", [(0, 0), (455, 0.0019045625784847), (1234.5342, 0.0051675772289661)])
def test_get_moon_lengths(test_input, expected):
    assert custom.get_moon_lengths(test_input) == expected

