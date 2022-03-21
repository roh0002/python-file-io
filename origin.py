""" 
Searches text for heritability related terms, returns term and the associated line number.

Variables:
    re_string: regex search string
    line_num: line number 
    in_stream: input text file (to search)
    out_stream: output text file (line number, regex match; tab-deliminated)

"""


import re

# Variables ####
re_string = r'[a-z]*herit[a-z]*'
line_num = 0
###############


print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening inherit.txt')
    with open('inherit.txt', 'w') as out_stream:
        re_object = re.compile(re_string, re.IGNORECASE)

        for line in in_stream:
            line_num = line_num + 1
            line = line.strip()
            word_list = line.split()
            hits = re.findall(re_object, line)

            if hits:
                for x in hits:
                    out_stream.write(str(line_num) + '\t{0}\n'.format(x)) 
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('inherit.txt is closed?', out_stream.closed)
