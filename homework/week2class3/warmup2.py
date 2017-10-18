my_list = [1, 'hello', 2, 'there', 3, 'list']
print(my_list[1])

print('#1')
print("My list will print 'hello'")
print(my_list[0])
print("Indices start at 0")

print('#2')
print(my_list[1::2])
#its a list

print('#3')
my_list.append(4)
print(my_list)

print('#4')
print(my_list[::2])

print('#5')
my_list.remove('list')
print(my_list)

print('#6')
print(my_list[1::2])

print('#7')
my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('Add the number 4 to mylist (y/n)? ')
if 'y' in user_input.lower():
    my_list.append(4)
print(my_list)

print('#8')
my_list = [1, 'hello', 2, 'there', 3, 'list']
user_input = input('What would you like added to the list (max 8 char)? ')
if len(user_input) < 8:
    my_list.append(user_input)
else:
    my_list.append(4)
print(my_list)
