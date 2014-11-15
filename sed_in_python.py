def sed(pattern, replacement, file_one, file_two):
    """ A funciton similar to the Unix sed program, i.e.
    get a pattern and a replacement strings if the pattern exists, 
    replace it with the string, if opening a file does not work, raise an exception """
    tetry :
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


