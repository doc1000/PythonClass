def calc_beers_on_the_wall(n=99):
       """Print how many beers remain on the wall.

       Args:
           n: int
               Holds the number of beers that remain on the wall.
        """
       return 'There are %(n)s bottles of beer on the wall' % locals()



#print(calc_beers_on_the_wall())

def check_elsa_fan(fan=True):
       """Print a certain phrase depending on the value of fan.

       Args:
           fan: boolean
       """
       if fan == True:
           return 'I Love Elsa!'
       else:
           return "Let It Go, it's not that great."

    #        return "Let It Go, it's not that great."

#print(check_elsa_fan(True))

def say_hello(name='Josh'):
    """ prints hello <name>
    Args: name: string

    """
    print('Hello {}'.format(name))

def is_divisor(n, potential_divisor=2):
    """determines if a number is a divisor of initial number
    Args: n: numerator
            potential_divisor: well, yea...
    """
    return n % potential_divisor == 0


def sum_down(my_num):
    """Write a script that computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down. This answer will look very much like the example above, you'll just need to change a couple of things.
    print('We will sum the numbers from 0 to your number.\r\n')

    my_num = int(input("What is your number: "))
    """
    total = 0
    counter = my_num
    while counter > 0:
        total += counter
        counter -= 1
    return 'The sum is: ' + str(total)

def calc_factorial(my_num):
    """Write a script that computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down. This answer will look very much like the example above, you'll just need to change a couple of things.
    print('We will calculate the factorial your number.\r\n')
    my_num = int(input("What is your number: "))
    """
    total = 1
    counter = my_num
    while counter > 0:
        total *= counter
        counter -= 1
    return 'The factorial is: ' + str(total)

def calc_lcm(my_num,sec_num):
    """Write script to calc LCM of two integers
    print('We will determine the least common multiple of 2 numbers')
    my_num = int(input('First number: '))
    sec_num = int(input('Second number: '))
    """
    lcm = my_num * sec_num
    counter = sec_num-1
    while counter > 1:
        ncm = my_num * counter
        if ncm%sec_num == 0:
            lcm = ncm
        counter -= 1

    return 'The LCM is ' + str(lcm)
