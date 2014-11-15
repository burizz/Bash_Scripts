
def has_duplicates(a_list):
    new_list = []
    for item in a_list:
        if item not in new_list:
            print item
            new_list.append(item)
            print new_list
    if sorted(new_list) == sorted(a_list):
        return True
    else:
        return False

def walk_os_dirs(dirname):
    """ "Walks" through a directory, prints the names of all files, and calls itself recursively on all the directories. """
    import os

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk_os_dirs(path)




# class Time(object):
#     """ Represents the time of day.
#
#     attributes: hour, minute, day
#     """
#
# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30
#
# def print_time(time_object):
#     print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
#
# print_time(Time)

# ======================================================================================================================================================================================
#
# def checkio(array):
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     list_even_index_values = []
#     last_element = len(array) - 1
#
#     if len(array) == 0:
#         return 0
#     for item in range(0, len(array)):
#         if item % 2 == 0:
#             list_even_index_values.append(array[item])
#
#     total = sum(list_even_index_values) * array[last_element]
#
#     return total
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "Empty"
#
# ====================================================================================================================================================================================================


import requests
import re

user_input = str(raw_input("Zip Code? "))

def is_len_valid(user_input):
    return len(user_input) == 5

def is_all_num(user_input):
    flag = True
    for char in user_input:
        if not char.isdigit():
            flag = False
            return flag
    return flag

#def is_query_valid(data):
# return "<title>" in data_list[1]

def main():
    if not is_len_valid(user_input):
        print "The input must have 5 digits"
    elif not is_all_num(user_input):
        print "Zip Codes don't have letters!"
    # elif not is_query_valid(data):
    # print "Information for %s not found." % user_input
    else:
        city = re.findall(r'\<h2\>\<strong\>(.*?),\ ', data)
        population = re.findall(r'Total\ population\</dt\>\<dd\>(.*?)\<', data)
        print "%s (%s) has a population of %s" % (city[0], user_input, population[0])

data = requests.get("http://www.uszip.com/zip/" + user_input).content
data_list = [line for line in data.splitlines()]
main()


# <p>
# Then go to www.uszip.com, which provides information about every zip code
# in the country.  For example, the URL

# <p>
# http://www.uszip.com/zip/02492

# <p>
# provides information about Needham MA, including population, longitude
# and latitude, etc.

# <p>
# Write a program that prompts the user for a zip code and prints the
# name and population of the corresponding town.

# <p>
# Note: the text you get from uszip.com is in HTML, the language most
# web pages are written in.  Even if you don't know HTML, you should be
# able to extract the information you are looking for.


