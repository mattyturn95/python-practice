## designed to count the number of upper case letters in a text/string

def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count


assert count_upper_case("") == 0, "no uppercase characters"
assert count_upper_case("A") == 1, "One Uppercase Letter"
assert count_upper_case("a") == 0, "one Lowercase Letter"
assert count_upper_case("@$#%^") == 0, "Special Characters"

print("All the Tests Passed")