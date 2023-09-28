from address import extract_city,extract_state,extract_zipcode
import pytest

dirs = [
    "123 Main Street, Los Angeles, CA 90001",
    "456 Elm Avenue, New York, NY 10001",
    "789 Oak Road, Chicago, IL 60601",
    "101 Pine Lane, Houston, TX 77002",
    "222 Maple Street, Miami, FL 33101"
]

def test_extract_zipcode():
    for dir in dirs:
        assert extract_zipcode(dir) == dir.split(",")[2].split(" ")[2]

def test_extract_state():
    for dir in dirs:
        assert extract_state(dir) == dir.split(",")[2].split(" ")[1]

def test_extract_city():
    for dir in dirs:
        assert extract_city(dir) == dir.split(",")[1].strip()

pytest.main(["-v", "--tb=line", "-rN", __file__])