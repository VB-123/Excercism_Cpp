def is_valid(isbn):
    nums = []
    
    # Removing dashes from the input string
    isbn = isbn.replace('-', '')
    
    # Making the numbers list
    for index in range(len(isbn)):
        if isbn[index].isdigit() :
            nums.append(int(isbn[index]))
        elif index == len(isbn) - 1 and isbn[index] == 'X':
            nums.append(10)
        else:
            return False

    # Checking invalid Input
    if len(nums) != 10:
        return False 
        
    # Validating ISBN Code
    digits_sum = sum(nums[index]*(10 - index) for index in range(len(nums)))
    return True if digits_sum % 11 == 0 else False
