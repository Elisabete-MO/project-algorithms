# from challenges.challenge_encrypt_message import encrypt_message
import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Test case 1: Valid odd key
    message = "Hello, World!"
    key = 3
    encrypted = encrypt_message(message, key)
    assert encrypted == "leH_!dlroW ,ol"

    # Test case 2: Valid even key
    message = "OpenAI is amazing"
    key = 6
    encrypted = encrypt_message(message, key)
    assert encrypted == "gnizama si _IAnepO"

    # Test case 3: Invalid key type (string)
    message = "Hello"
    key = "invalid"
    with pytest.raises(TypeError):
        encrypt_message(message, key)

    # Test case 4: Invalid key type (float)
    message = "Hello"
    key = 2.5
    with pytest.raises(TypeError):
        encrypt_message(message, key)

    # Test case 5: Invalid key (invalid value)
    message = "OpenAI is amazing"
    key = -2
    encrypted = encrypt_message(message, key)
    assert encrypted == "gnizama si IAnepO"

    # Test case 6: Invalid message (type is not string)
    message = 12345
    key = 10
    with pytest.raises(TypeError):
        encrypt_message(message, key)

    # Test case 7: Invalid key (type is not a number)
    message = "Hello"
    key = "ABC"
    with pytest.raises(TypeError):
        encrypt_message(message, key)

    print("All test cases passed!")
