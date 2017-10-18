# Write a script that computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down. This answer will look very much like the example above, you'll just need to change a couple of things.

print('#1. We will calculate the factorial your number.\r\n')

my_num = int(input("What is your number: "))

total = 1

#while counter > 0:
for counter in range(1,my_num+1):
    total *= counter
    print('*' + str(counter) + ' = ' + str(total))

print('\r\nThe factorial is: ' + str(total))


my_num = int(input('What number do want to check if its prime: '))
divisor = 0
for counter in range(2,my_num):
  if my_num%counter == 0:
    divisor = counter

    if divisor != 0:
        break

if divisor == 0:
    print("The number you inputted is a prime number")
else:
    print("The number you inputted is not a prime number")
