def is_reverse(first_word, second_word):
    """ Verify that the first word is the same as the second word reversed """
    if len(first_word) != len(second_word):
        return "Not the same as the first word !"

    fwd_count = 0
    bckwd_count = len(second_word) - 1

    while bckwd_count > 0:
        if first_word[fwd_count] == second_word[bckwd_count]:
            fwd_count += 1
            bckwd_count -= 1
        else:
            return "Not the same as the first word !2"
    return first_word +  " is the same as " + second_word + " reversed !"


def word_count(lst, word):
    """ Count the occurences of the word in a list """
    word = word.lower()
    count = 0
    lst_indx = 0
    position = len(lst) - 1
    while position > 0:
        if word == lst[lst_indx]:
            count += 1
            lst_indx += 1
            position -= 1
        else:
            lst_indx += 1
            position -= 1
    return count



def word_list():
    """ Get a file with words and make it into a list """
    words = open(raw_input('Enter filename :'), 'r')
    lst = []
    for item in words:
        lst.append(item.strip())   #strip() removes the \n that are added by the encoding
    return lst


def has_no_e(file_name):
    """Get a file as input and return the amount of words that have the letter 'e' in them """
    words = open(file_name, 'r')
    count = 0
    for item in words:
        if 'e' in item:
            print item
            count += 1
    return count


def is_sorted(a_list):
    """ Get a list as input, return True if list is sorted and False otherwise."""
    sorted_list = sorted(a_list)
    if sorted_list == a_list:
        return True
    else:
        return False

def is_anagram(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False


def words_from_text(file_with_text):
    """ Open a file with text and return the number of words and the amount of different words in the text """
    import string

    text = open(file_with_text, 'r')

    words = []
    amount_of_words = 0
    number_different_words = 0

    for line in text:
        line = line.replace('-',' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            if word not in words:
                number_different_words +=1
            words.append(word)
            amount_of_words += 1


    return  (" This book has a total of %s words. It has %s different words !") % (amount_of_words, number_different_words)

print "-- Perlycross -- \n" + words_from_text('project_gutenberg.txt')
print " \n \n "
print "-- Life and Adventures of 'Billy' Dixon -- \n" + words_from_text('project_gutenberg_2.txt')

def robeco_travel(amount_of_people):
    """ Calculate travel expenses for Robeco travel """
    days = int(raw_input("Enter days of the travel : "))
    flight_price = float(raw_input("Enter Plane ticket price : "))
    train_price = float(raw_input("Enter Train icket price : "))
    hotel_price = float(raw_input("Enter Hotel price per night : "))
    daily_accomodation = int(raw_input("Enter Daily accomodation amount : "))

    total = (flight_price + train_price + ( hotel_price * days ) + ( daily_accomodation * days )) * amount_of_people

    print "The total amount of money for %d people is %d EUR !" % (amount_of_people, total)

#########################################################################################################
# The rest are not completely tested
#########################################################################################################

def ArrayAdditionI(arr):
    """
    Take arr and check if the highest number in
    arr == to the sum of the rest of the numers.
    ex.[4, 6, 23, 10, 1, 3]
    return 'true' if  4 + 6 + 10 + 3 = 23
    """

    nums = sorted(arr)

    #Get highest num
    highestNum = max(arr)
    currentSum = 0 - highestNum

    for num in nums:
        currentSum += num

    if currentSum < highestNum:
        return 'false'
    else:
        return 'true'

def common_words(first, second):
    """ Get two strings of words and return the words that occur in both strings """

    # Split the strings into lists of words
    first_words = first.split(',')
    second_words = second.split(',')

    duplicate_words = []

    # Check if there are duplicate words in the lists
    for item in first_words:
        if item in second_words:
            duplicate_words.append(item) # Create a list of the duplicate words

    result = ','.join(sorted(duplicate_words))

    if len(duplicate_words) == 0:
        print "There are no common words in the two strings."

    return result

def absolute_sort(numbers_array):
    return sorted(numbers_array, key=lambda x: abs(x))

def Progression(arr):
    """
    Check if arr is a list of numbers that are in Arithmetic, Geometric or without any progression.
    Exmaple :
    return "Arithmetic" if ex. [2, 4, 6, 8]
    return "Geometric" if ex. [2, 6, 18, 54]
    return -1 if none
    """

    # Check if array is with at least 3 elements
    if len(arr) < 3: return 0

    # Calculate difference between numbers in list
    diffAr = arr[1] - arr[0]
    diffGeo = arr[1] / arr[0]

    # Temp vars to check if list is in progression
    isA = True
    isG = True

    for num in range(1, len(arr)):
        if arr[num] - arr[num - 1] != diffAr:  #Check if progression is Arithmetic
            isA = False
        if arr[num] / arr[num -1] != diffGeo:  #Check if progression is Geometric
            isG = False

    if isA:
        return "Arithmetic"
    elif isG:
        return "Geometric"
    else:
        return "-1"

# Test function
print Progression([2, 4, 16, 24])
print Progression([5, 10, 15])
print Progression([2, 6, 18, 54])
print Progression([2, 6])


# Palindrome Checker Program
import stack

# welcome

print ('This program can determine if a given string is a palindrome')
print ('(Enter return to exit)')

#init

char_stack = stack.getStack()
empty_string = ''

#get string from user

chars = input('Enter string to check')

while chars != empty_string:
    if len(chars) == 1:
        print ('A one letter word is by definition a palindrome\n')

    else:
        #init
        is_palindrome = True

        # to handle strings of odd lenght
        compare_lenght = len(chars) // 2

        # push second half of input string on stack
        for k in range(compare_lenght, len(chars)):
            stack.push(char_Stack, chars[k])

        # pop chars and compare to first half of string
        k = 0
        while k < compare_lenght and is_palindrome:
            ch = stack.pop(char_Stack)
            if chars[k].lower() != ch.lower():
                is_palindrome = False

            k = k + 1

        # display results
        if is_palindrome:
            print(chars, 'is a palindrome \n')
        else:
            print(chars, 'is NOT a palindrome\n')

    # get next string from user
    chars = input('Enter string to check: ')
