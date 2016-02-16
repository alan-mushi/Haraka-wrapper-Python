from ctypes import *


def haraka512(msg: bytes) -> bytes:
    assert len(msg) == 64

    lib = cdll.LoadLibrary('./libharaka.so')
    h = create_string_buffer(b'A' * 32)
    lib.haraka512256(h, create_string_buffer(msg))
    _hash = b''

    for i in range(32):
        _hash += h[i]

    return _hash


def haraka256(msg: bytes) -> bytes:
    assert len(msg) == 32

    lib = cdll.LoadLibrary('./libharaka.so')
    h = create_string_buffer(b'A' * 32)
    lib.haraka256256(h, create_string_buffer(msg))
    _hash = b''

    for i in range(32):
        _hash += h[i]

    return _hash


if __name__ == '__main__':
    print("Testing Haraka256: " + str(haraka256(bytes([i for i in range(32)])).hex() == "cbb4e2a4a7b471c6cc448cd264d1083eaf8f75d0d40ac4f973da6d53bfc05cc0"))
    print("Testing Haraka512: " + str(haraka512(bytes([i for i in range(64)])).hex() == "2f62a31be6eb3a1cd643fea5e869ff7cbe863b265db4b00e7cf3e319bfa166c1"))
