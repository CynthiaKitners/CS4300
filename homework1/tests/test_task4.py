import pytest

#variables
cost = 5
Number_of_Product = 10

Total = float(cost) * int(Number_of_Product)
Discount = float(Total) * 0.1
FinalCost = float(Total) - float(Discount)

def test_discount():
    assert Total == 50
    assert Discount  == 5.00
    assert FinalCost == 45.0 