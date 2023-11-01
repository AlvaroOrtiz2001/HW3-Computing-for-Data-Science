import pytest
from hw3 import compute_distance

def test_compute_distance():
    test_coords = [((41.23,23.5), (41.5, 23.4)),((52.38, 20.1),(52.3, 17.8))]
    result = compute_distance(test_coords)
    expected = [31.131865222052042, 157.005827868894]
    assert result == pytest.approx(expected), "Incorrect result"

