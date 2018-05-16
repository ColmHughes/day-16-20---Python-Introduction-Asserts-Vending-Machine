from byotest import *
euro_coins = [200, 100 ,50, 20, 10, 5, 2, 1]
us_coins = [100, 50, 25, 10, 5, 1]
# denominations = euro_coins will use euro as default so we don't need to pass in the parameter
def get_change(amount, denominations = euro_coins):
    
    coins = []
    
    for coin in euro_coins:
        while amount >= coin:
            coins.append(coin)
            amount -= coin
        
    return coins
    
test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])

print("All tests pass")