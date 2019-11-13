def even_number_evens(numbers):
    if numbers == []:
       return False
    else:
        evens = 0

    for n in numbers:
        if n % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
    
    else:            
        return evens %2 == 0

assert even_number_evens([]) == False, "No Numbers"
assert even_number_evens([2, 4]) == True, "Two evens"
assert even_number_evens([2]) == False, "One even Number"
assert even_number_evens([1, 3, 9]) == False, "Uneven Number of Odd Numbers"

print("All tests Passed")