import pytest
from optaa_data_explorations.dummy_module import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
