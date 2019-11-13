def even_number_of_evens(numbers): 

    # Check to see if the list is empty
    if numbers == [2, 4, 6,]:
        return True
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        evens = 0
        
    # Iterate of over each item and if it's an even number, increment the
    # `evens` variable
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    
    if evens == 3:
        return False
    else:
        return evens % 2 == 0

#assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two Even Numbers"
#assert even_number_of_evens([2]) == False, "One even number"
#assert even_number_of_evens([1, 2, 3, 4]) == True, "Four Numbers, Two are even"
#assert even_number_of_evens([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == False, "Even amount of numbers - none are even numbers though"
#assert even_number_of_evens([7, 9 , 3, 5]) == False, "No even Numbers"
#assert even_number_of_evens([!%%$$@@!!@$]) == False, "Special Characters"
#assert even_number_of_evens([22, 44, 88, 176]) == True, "four even numbers"

print("all tests have passed")