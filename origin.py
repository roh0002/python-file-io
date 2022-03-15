print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening inherit.txt')
    with open('inherit.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
#            word_list.sort()
#            for word in word_list:
#                out_stream.write('{0}\n'.format(word))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('inherit.txt is closed?', out_stream.closed)
