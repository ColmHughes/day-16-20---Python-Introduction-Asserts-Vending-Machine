from byotest import *



def even_number_of_evens(l):
    if len([ l for x in l if x % 2 == 0]) % 2 == 0:
        return True
    else:
        return False
    
    
test_are_equal(even_number_of_evens([]), True)    
    
# assert even_number_of_evens([]) == True, "Empty list"
# assert even_number_of_evens([2, 5]) == False, "One even number"
# assert even_number_of_evens([4, 8, 1]) == True, "Two even numbers"
# assert even_number_of_evens([12, 8, 14, 2]) == True, "Four even numbers"
# assert even_number_of_evens([12, 8, 14]) == False, "Three even numbers"
# assert even_number_of_evens([1, 13, 5, 9]) == True, "No even numbers"
# assert even_number_of_evens([1, 13, 5]) == True, "No even numbers"
# assert even_number_of_evens([-2, -4]) == True, "Two even numbers"
# assert even_number_of_evens([0, 2]) == True, "Two even numbers"


print("All tests pass")