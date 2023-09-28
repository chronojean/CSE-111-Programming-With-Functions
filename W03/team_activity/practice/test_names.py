from names import make_full_name, extract_given_name, extract_family_name
import pytest

names = [
    ["Lissette", "Martínez"],
    ["Jean-Paul", "Andrade"],
    ["María del Rosario Concepción Ángeles", "Rodríguez"],
    ["Nancy", "Higuera"],
    ["Sarah","Connor"]
]

def test_make_full_name():
    for first_name, last_name in names:
        assert make_full_name(first_name,last_name) == f"{last_name}; {first_name}"

def test_extract_given_name():
    for first_name, last_name in names:
        assert extract_given_name(f"{last_name}; {first_name}") == first_name

def test_extract_family_name():
    for first_name, last_name in names:
        assert extract_family_name(f"{last_name}; {first_name}") == last_name

pytest.main(["-v", "--tb=line", "-rN", __file__])