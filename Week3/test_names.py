from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # full_name = full_name("Brown; Sally")
    # assert isinstance(full_name, str), "Make Full name function must return a string"

    
    assert make_full_name("Tom", "Cruise") == "Cruise; Tom"
    assert make_full_name("Brad", "Pitt") == "Pitt; Brad"

def test_extract_family_name():
    assert extract_family_name("Brown; Bobby") == "Brown"
    assert extract_family_name("Cruise; Tom") == "Cruise"
    assert extract_family_name("Pitt; Brad") == "Pitt"

def test_extract_given_name():
    assert extract_given_name("Brown; Bobby") == "Bobby"
    assert extract_given_name("Cruise; Tom") == "Tom"
    assert extract_given_name("Pitt; Brad") == "Brad"



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
