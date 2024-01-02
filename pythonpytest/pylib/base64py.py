import base64

def encoding(string):
    """
    Encode string as base64.
    """
    return base64.b64encode(string.encode())

def decoding(string):
    """
    Decode string as base64.
    """
    return base64.b64decode(string).decode()

