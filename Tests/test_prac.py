import pytest

def test_check():
    try:
        
        assert 7 == 7
        assert 1 == 2
    # many more statements like this
    except AssertionError:
        print('error meassage')            
 