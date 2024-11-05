# name: Christopher Groves

import pytest
from grades import calculate_average, determine_grade

def test_calculate_average():
    assert calculate_average([90,80,70]) == 80.0
    assert calculate_average([100]) == 100.0
    assert calculate_average([0]) == 0.0
    with pytest.raises(ValueError):
        calculate_average([])
    with pytest.raises(ValueError):
        calculate_average([85,95,110])
    assert calculate_average([0.01,99.99]) == 50.0

def test_determine_grade():
    assert determine_grade(90) == "B"
    assert determine_grade(95) == "A"
    assert determine_grade(80) == "B"
    assert determine_grade(70) == "C"
    assert determine_grade(60) == "D"
    assert determine_grade(59) == "F"

if __name__ == "__main__":
    test_calculate_average()
    test_determine_grade()