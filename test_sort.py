import pytest
from sort import sort


def test_standard():
    assert sort(10, 10, 10, 5) == "STANDARD"


def test_heavy_only():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_bulky_by_volume():
    assert sort(100, 100, 100, 5) == "SPECIAL"


def test_bulky_by_width():
    assert sort(150, 10, 10, 5) == "SPECIAL"


def test_bulky_by_height():
    assert sort(10, 150, 10, 5) == "SPECIAL"


def test_bulky_by_length():
    assert sort(10, 10, 150, 5) == "SPECIAL"


def test_rejected_bulky_and_heavy():
    assert sort(150, 150, 150, 20) == "REJECTED"


def test_boundary_volume_just_under():
    assert sort(99, 100, 100, 5) == "STANDARD"


def test_boundary_volume_exact():
    assert sort(100, 100, 100, 5) == "SPECIAL"


def test_boundary_mass_just_under():
    assert sort(10, 10, 10, 19) == "STANDARD"


def test_boundary_mass_exact():
    assert sort(10, 10, 10, 20) == "SPECIAL"


def test_boundary_dimension_just_under():
    assert sort(149, 10, 10, 5) == "STANDARD"


def test_boundary_dimension_exact():
    assert sort(150, 10, 10, 5) == "SPECIAL"
