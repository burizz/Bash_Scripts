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