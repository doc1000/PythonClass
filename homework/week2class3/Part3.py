print('#1')
my_num = int(input('What is the max number?:'))
return_num = []

for i in range(my_num+1):
    if i%2 == 0:
        return_num.append(i)
print(return_num)

print('#2')
my_num = int(input('What is the max number?:'))
my_div = int(input('What is the divisor?:'))
return_list = []

for i in range(my_num+1):
    if i%my_div == 0:
        return_list.append(i)
print(return_list)

print('#3')
list1 = [0, 3, 6, 9, 10, 2, 5]
list2 = [2, 6, 4, 7, 8, 1, 15]

new_list = []
for el in list1:
    if el in list2:
         new_list.append(el)
new_list.sort()
print(new_list)


print('#4')
my_num = int(input('What is the max number?:'))
my_mult = int(input('What is the base multiple?:'))
new_list = []
multiplier = 1

while multiplier*my_mult < my_num:
    new_list.append(multiplier*my_mult)
    multiplier += 1
print(new_list)



Print('#EC')
list1 = []
list2 = []
for i in range(7):
    list1.append(int(input('For List 1 what is element %(i)s of 0:6?:' % locals())))
for i in range(7):
    list2.append(int(input('For List 2 what is element %(i)s of 0:6?:' % locals())))
new_list = []
for el in list1:
    if el in list2:
         new_list.append(el)
new_list.sort()
print(new_list)
