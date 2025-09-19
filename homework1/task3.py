#this file will check to see if a given number is positive, negative, or zero
import pytest
def check_number(num):
    if(num) > 0:
        print("positive")
    if(num) < 0:
        print("negative")
    if(num) == 0:
        print("zero")    
check_number(0)
check_number(98)
check_number(-77)

#=======================================================================

def test_num():
    assert -8 < 0
    assert 38 > 0
    assert 0 == 0