#1
my_list = input("List numbers separated by commas (ie '1,2,3,4'): ").split(',')
my_set = set(my_list)
my_list = input("Second list numbers separated by commas (ie '1,2,3,4'): ").split(',')
my_set2 = set(my_list)
#my_set2 = {x for x in input("Second list numbers separated by commas (ie '1,2,3,4'): ").split(','))}
print( ",".join(my_set.intersection(my_set2)))


#2
my_list = input("List word separated by commas (ie 'one,two,three'): ").split(',')
my_set = {x.strip() for x in my_list}
print(",".join(my_set))


#3
my_set = set()
my_word = ''
while my_word != 'q':
    my_word = input("Enter a word: ")
    if my_word == 'v':
        print(",".join(my_set))
    else:
        my_set.add(my_word)
