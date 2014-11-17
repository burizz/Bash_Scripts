# Sparse Text program

def createModifiedFile (input_file, outputfile):
    
    """ For next file input_file, creates a new version in file outputfile
         in which all instances of the letter 'e' are removed.
    """
    
    empty_str=''
    num_total_chars = 0
    num_removals = 0
    
    for line in input_file:
        
        #Save original line length
        orig_line_length = len(line) - 1
        num_total_chars = num_total_chars + orig_line_length
        
        #remove all occurances of letter 'e'
        modified_line = line.replace('e', empty_str).replace('E', empty_str)
        num_removals = num_removals + \
                         (orig_line_length - (len(modified_line)-1))
        
        #simultaneously output live to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)
        
    return (num_total_chars, num_removals)

# --- Main

# program greeting

print (' This program will display the contents of a provided text file')
print ('with all ocurrances of the letter "e" removed.\n')

#open files for reading

file_name = raw_input('Enter file name (including file extension): ')
input_file = open(file_name, 'r')
new_file_name = 'e_' + file_name
output_file = open(new_file_name, 'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, 'occurances of the letter e removed')
print('Percentage of data lost:' , int((num_removals / num_total_chars) * 100), '%')

#