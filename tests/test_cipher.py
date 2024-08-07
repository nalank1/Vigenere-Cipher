def test_encryption():
    from app import encrypt
    assert encrypt("HELLO", "KEY") == "RIJVS"
    assert encrypt("WORLD", "KEY") == "JVSZL"

    # Test with different cases and empty string
    assert encrypt("hello", "key") == "RIJVS"
    assert encrypt("", "KEY") == ""

    # Test key shorter than text
    assert encrypt("LONGMESSAGE", "KEY") == "LQTRJXTBKGBI"

    # Test key longer than text
    assert encrypt("SHORT", "THISISALONGKEY") == "DLOQH"

def test_decryption():
    from app import decrypt
    assert decrypt("RIJVS", "KEY") == "HELLO"
    assert decrypt("JVSZL", "KEY") == "WORLD"

    # Test with different cases and empty string
    assert decrypt("rijvs", "key") == "HELLO"
    assert decrypt("", "KEY") == ""

    # Test key shorter than text
    assert decrypt("LQTRJXTBKGBI", "KEY") == "LONGMESSAGE"

    # Test key longer than text
    assert decrypt("DLOQH", "THISISALONGKEY") == "SHORT"

