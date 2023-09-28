from practice.address import extract_city,extract_state,extract_zipcode
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
        assert extract_zipcode(dir) == dir[-5:]

def test_extract_state():
    for dir in dirs:
        assert extract_state(dir) == dir[-8:-6]


pytest.main(["-v", "--tb=line", "-rN", __file__])



























# def test_extract_state():
#     assert extract_state(dirs[0])=="CA"
#     assert extract_state(dirs[1])=="NY"
#     assert extract_state(dirs[2])=="IL"
#     assert extract_state(dirs[3])=="TX"
#     assert extract_state(dirs[4])=="FL"

# def test_extract_zip_code():
#     assert extract_zipcode(dirs[0])=="90001"
#     assert extract_zipcode(dirs[1])=="10001"
#     assert extract_zipcode(dirs[2])=="60601"
#     assert extract_zipcode(dirs[3])=="77002"
#     assert extract_zipcode(dirs[4])=="33101"

# pytest.main(["-v", "--tb=line", "-rN", __file__])
