print('#1')
my_letter = input('What letter to search for?:')
my_string = input('What string to search?:')
print(my_string.lower().count(my_letter.lower()))
counter = 0
for some_letter in my_string.lower():
    if some_letter == my_letter.lower():
        counter += 1
print(counter)

print('#2')
my_string = input('What string to search?:')
if my_string[len(my_string)-1] == '!':
    print(my_string[:-1].upper())
else:
    print(my_string.lower())

print('#3')
my_string = input('What string to search?:')
vowel = ('a','e','i','o','u')

for v in vowel:
    my_string = my_string.replace(v,'')
    V = v.upper()
    my_string = my_string.replace(V,'')
print(my_string)

print('#4')
my_string = input('What string to search?:')
new_string = ''
for i,letters in enumerate(my_string):
    if (i+2)%2 == 0:
        new_string += letters.upper()
    else:
        new_string += letters
print(new_string)
