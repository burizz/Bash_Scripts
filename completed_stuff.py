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
    
   
    
def sed(pattern, replacement, file_one, file_two):
    """ A funciton similar to the Unix sed program, i.e.
    get a pattern and a replacement strings if the pattern exists, 
    replace it with the string, if opening a file does not work, raise an exception """
    try :
        initial_file = open(file_one, 'r')
        final_file = open(file_two, 'w')

        for item in initial_file:
            item = item.replace(pattern, replacement)
            final_file.write(item)
        
        initial_file.close()
        final_file.close()

    except IOError:
        print "Can't open or write to file"
    else:
        print "Replaced occurances of %s with %s successfully" % (pattern, replacement)



