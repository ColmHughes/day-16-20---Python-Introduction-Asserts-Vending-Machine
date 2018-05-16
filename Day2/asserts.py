# x = 2
# y = 1

# assert y > x, "y should be greater than x, but y is {0} and x is {1}".format(y, x)

# print(x + y)

# def count_upper_case(message):
#   count = 0
#   for c in message:
#       if c.isupper():
#           count += 1
#   return count

# assert count_upper_case("") == 0, "Empty string"
# assert count_upper_case("A") == 1, "One upper case"
# assert count_upper_case("a") == 0, "One lower case"
# assert count_upper_case("£$%%^") == 0, "Special characters"
# assert count_upper_case("ALLCAPS") == 7, "7 capitals"
# assert count_upper_case("300") == 0, "300 has no caps"





def count_upper_case(message):
   l = [c for c in message if c.isupper()]
   return len(l)

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("ALLCAPS") == 7, "7 capitals"
assert count_upper_case("300") == 0, "300 has no caps"

print("All the tests passed")











