def sum_even_add_last(array):
    """
    Return sum of the values on each even index * the value of the last index
    
    example : [1, 3, 5] is (1+5)*5 = 30
    """
    list_even_index_values = []
    last_element = len(array) - 1
    
    if len(array) == 0:
        return 0
    for item in range(0, len(array)):
        if item % 2 == 0:
            list_even_index_values.append(array[item])

    total = sum(list_even_index_values) * array[last_element]
    
    return total


def three_words(words):
    """
    Return True if the string "words" has 3 consecutive words and false otherwise.
    
    example : [test, 2, testing] = False
              [test, testing, tested] = True
    """
    words = words.split()
    count = 0
    
    if len(words) < 3:
        return False
    
    for item in words:
        if count == 3:
            return True
        elif item.isalpha():
            count += 1
        elif count < 3 and item.isdigit():
            count = 0
    return False


def most_numbers(*args):
    """
    Return the difference between the max and min values of a list with arbitrary length.
    
    example : [1, 3.14529, 4, 5] is 5 - 1 = 4
    """
    arg_list = []
    for item in args:
        arg_list.append(item)
    
    if len(arg_list) == 0:
        return 0

    return max(arg_list) - min(arg_list)


def digit_multiplication(number):
    """
    Return the total of all elements above 0 of 'number' multiplied.
    
    example : 123056 is 1*2*3*5*6 = 180
    """
    number = str(number)
    total = 1
    number_list = []
    
    for item in number:
        if item != '0':
            number_list.append(int(item))
            
    for item in number_list:
        total *= item 

    return total


def number_of_unities(number):
    """
    Get an integer, convert to binary and return the number of unities(1).
    """
    binary = bin(number)
    return str(binary).count('1')


def number_base(str_number, radix):
    """
    Get a positive number as a String and a Radix for it. If the Radix is <= 37 and >= 2 return it in decimal form. 
    
    example : number_base("AF", 16) -> returns 175 ( This is  "Hex" ), number_base("101", 5) returns 26 (This is base 5)
    """
    number = 0
    if radix <= 37 and radix >= 2:
        try:
            number = int(str_number, radix)
            return number
        except ValueError:
            return -1
