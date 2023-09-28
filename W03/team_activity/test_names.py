from practice.names import make_full_name, \
    extract_family_name, extract_given_name
import pytest
names = [
    ["Lissette", "Martínez"],
    ["Jean", "Andrade"],
    ["María", "Rodríguez"],
    ["Nancy", "Higuera"]
]
def test_make_full_name():
    for firstname, lastname in names:
        assert make_full_name(firstname, lastname) == f"{firstname}; {lastname}"
        
def test_extract_family_name():
    for name in names:
        assert extract_family_name(f"{name[1]}; {name[0]}") == name[1]
        
def test_extract_given_name():
    for name in names:
        assert extract_given_name(f"{name[1]}; {name[0]}") == name[0]
        
pytest.main(["-v", "--tb=line", "-rN", __file__])