import pytest
from app import encrypt, decrypt

def test_encryption():
    
    assert encrypt("HELLO", "KEY") == "RIJVS"
    assert encrypt("WORLD", "KEY") == "GSPVH"

    # Test with different cases and empty string
    assert encrypt("hello", "key") == "RIJVS"
    assert encrypt("", "KEY") == ""

    # Test key shorter than text
    assert encrypt("LONGMESSAGE", "KEY") == "VSLQQCCWYQI"

    # Test key longer than text
    assert encrypt("SHORT", "THISISALONGKEY") == "LOWJB"

def test_decryption():
    assert decrypt("RIJVS", "KEY") == "HELLO"
    assert decrypt("GSPVH", "KEY") == "WORLD"

    # Test with different cases and empty string
    assert decrypt("rijvs", "key") == "HELLO"
    assert decrypt("", "KEY") == ""

    # Test key shorter than text
    assert decrypt("VSLQQCCWYQI", "KEY") == "LONGMESSAGE"

    # Test key longer than text
    assert decrypt("LOWJB", "THISISALONGKEY") == "SHORT"

