import pytest

def identity(x):
    return x

def test_identity():
    assert identity(3) == 3

if __name__ == '__main__':
    test_identity()

# the quick brown fox jumped over the lazy dog