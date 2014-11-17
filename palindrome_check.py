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


#