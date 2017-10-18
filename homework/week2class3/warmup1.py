my_str = 'This String was not Chosen Arbitrarily...'
print(my_str.upper())

#Homework
print('#1')
print(my_str[14]) #returns 's'

print('#2')
my_str = my_str.replace('was not',"wasn't")
print(my_str[14]) #still returns 's'

print('#3')
print(my_str.lower())

print('#4')
my_str += ' oR wAs it??'
print(my_str.lower())

print('#5')
print(my_str[41:])

print('#6')
print(my_str[41:-1].upper())

print('#7')
my_str = 'This String was not Chosen Arbitrarily...'
user_input = input('Add "oR wAs it??" (y/n)? ')`
if 'y' in user_input.lower():
    my_str += ' oR wAs it??'
print(my_str)

print('#8')
my_str = 'This String was not Chosen Arbitrarily...'
user_input = input('String to add to end of my_str: ')
my_str += user_input
print(my_str)

print('#9')
my_str = 'This String was not Chosen Arbitrarily...'
user_input = input('String to add to end of my_str: ')
if len(user_input) < 10:
    my_str += user_input
print(my_str)
