# Duck typing the functionality of a language...a function that calculates the
# price of a product after apllying a given discount.   Use integers and floats
import pytest

#variables
cost = 5
Number_of_Product = 10

#calculator

Total = float(cost) * int(Number_of_Product)
Discount = float(Total) * 0.1
FinalCost = float(Total) - float(Discount)
print("Final price of: ", Number_of_Product, ": $", FinalCost)

#=======================================================================================




def test_discount():
    assert Total == 50
    assert Discount  == 5.00
    assert FinalCost == 45.0 
