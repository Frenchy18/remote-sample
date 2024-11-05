"""Unit test for meteoric.py
    pytest --cov --cov-branch --cov-report=html
    
    Authors: Vincent Baccari & Christopher Groves
"""
import meteoric
import pytest


test_meteors = [
    ["Aachen", "1", "Valid", "L5", "21", "Fell", "1880", "50.775", "6.08333"],
    ["Aarhus", "2", "Valid", "H6", "720", "Fell", "1951", "56.18333", "10.23333"],
    ["Abee", "6", "Valid", "EH4", "107000", "Fell", "1952", "54.21667", "-113"],
    ["Acapulco", "10", "Valid", "Acapulcoite", "1914", "Fell", "1976", "16.88333", "-99.9"],
]

def test_load_data():
    """Test case for load_data()"""
    result = meteoric.load_data()
    assert result[0] == ["Aachen", "1", "Valid", "L5", "21", "Fell", "1880", "50.775", "6.08333"]
    # assert result[4] == ["Acapulco", "10", "Valid", "Acapulcoite", "1914", "Fell" "1976", "16.88333", "-99.9"]

def test_year():
    assert meteoric.year(test_meteors, "1880") == 'The meteor Aachen ID: 1 Type: Valid Recclass: L5 Mass (g): 21 fall type: Fell landed at 50.775 and 6.08333.'
    assert meteoric.year(test_meteors, "1951") == 'The meteor Aarhus ID: 2 Type: Valid Recclass: H6 Mass (g): 720 fall type: Fell landed at 56.18333 and 10.23333.'
    assert meteoric.year(test_meteors, "1950") == "No meteors found for the year 1950"

def test_year_exceptions():
    with pytest.raises(ValueError) as verr:
        meteoric.year(test_meteors, "88") 
    assert str(verr.value) == '88 is invalid. Please enter a valid 4 digit year.'
    
    with pytest.raises(ValueError) as verr:
        meteoric.year(test_meteors , "-1")
    assert str(verr.value) == '-1 is invalid. Please enter a valid 4 digit year.'

    with pytest.raises(ValueError) as verr:
        meteoric.year(test_meteors , "10000")
    assert str(verr.value) == "10000 is invalid. Please enter a valid 4 digit year."

    with pytest.raises(ValueError) as verr:
        meteoric.year(test_meteors, None)
    assert str(verr.value) == "None is invalid. Please enter a valid 4 digit year."

    with pytest.raises(ValueError) as verr:
        meteoric.year(test_meteors, '')
    assert str(verr.value) == " is invalid. Please enter a valid 4 digit year."
    
    with pytest.raises(IndexError) as verr:
        meteoric.year(test_meteors, "5400")
    assert str(verr.value) == "5400 not within valid range."

def test_geo_point():
    assert meteoric.geo_point(test_meteors, "56.1833, 10.23333") == "The Meteor Aarhus with ID: 2 Named Type: Valid Recclass: H6 Mass (g): 720 and Fall Type: Fell landed closest to that location in: 1951"
    assert meteoric.geo_point(test_meteors, "54.21667,-113") == "The Meteor Abee with ID: 6 Named Type: Valid Recclass: EH4 Mass (g): 107000 and Fall Type: Fell landed closest to that location in: 1952"

def test_geo_point_exception():
    with pytest.raises(ValueError) as verr:
        meteoric.geo_point(test_meteors, "-100,189")
    assert str(verr.value) == 'Latitude and longitude is out of range.'

def test_find_recclass():
    assert meteoric.find_recclass(test_meteors, "H6") == "The Meteor Aarhus ID: 2"
    assert meteoric.find_recclass(test_meteors, "Acapulcoite") == "The Meteor Acapulco ID: 10"
    assert meteoric.find_recclass(test_meteors, "999999") == "No meteors found with that recclass"

def test_high_mass():
    assert meteoric.high_mass(test_meteors, "1") == "The meteor Abee ID: 6 Mass (g): 107000 Recclass: EH4"
    assert meteoric.high_mass(test_meteors, "2") == "The meteor Abee ID: 6 Mass (g): 107000 Recclass: EH4\nThe meteor Acapulco ID: 10 Mass (g): 1914 Recclass: Acapulcoite"
    
def test_high_mass_exceptions():
    with pytest.raises(ValueError) as err:
        meteoric.high_mass(test_meteors, "0")
    assert str(err.value) == "The number of meteorites must be greater than 0"

    # with pytest.raises(ValueError) as verr:
    #     meteoric.high_mass(test_meteors, "lame")
    # assert str(verr.value) == "Error converting mass to float. Mass values are invalid."

def test_count_class():
    assert meteoric.count_class(test_meteors) == "Fell: 4"


if __name__ == "__main__":
    pytest.main()    