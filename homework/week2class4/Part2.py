## 1
my_str = input("List numbers separated by dashes (ie '1 - 2 - 3 - 4'): ")

print({int(x): int(x)**2 for x in my_str.split("-")})




## 2
state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                        'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                        'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

my_state = input("What state would you like the capital of?: ").title()

print(state_dictionary.get(my_state,'Capital Unknown'))


#3
my_d = {}
my_coor = list('empty')
while len(my_coor)>0:
    my_coor = input("Please enter a coordinate-word pair in the format (x, y, word): ").split(",")
    if len(my_coor)==3:
        my_d[(int(my_coor[0]),int(my_coor[1]))] = my_coor[2]
    elif my_coor[0] == '':
        break


my_l = ''
while my_l != 'q':
    my_l = input('Please enter a coordinate to look up (ie 3,4 or q to quit): ').split(",")
    if len(my_l) != 2:
        break
    my_l = (int(my_l[0]),int(my_l[1]))

    if my_l in my_d:
        print(my_d.get(my_l))
    else:
        print('Coordinate not found')
