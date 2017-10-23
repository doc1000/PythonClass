# part 1

def calc_prime(my_num):
    """return True if prime, else False
    Args: my_num: int
    """
    return len([x for x in range(2,my_num) if my_num%x == 0])==0

def word_count(my_str):
    """
    counts words in string
    Args: my_str: string
    """
    return len(my_str.split(' '))

def word_count_delim(my_str,my_delim = ' '):
    """
    counts words in string
    Args: my_str: string
    """
    return len(my_str.split(my_delim))

def word_length_delim(my_str,my_delim = ' '):
    """
    counts words in string
    Args: my_str: string
    """
    return [len(x) for x in my_str.split(my_delim)]

def all_primes(my_num):
    """returns list of prime numbers up to my_num
    Args: my_num: int
    """
    return [x for x in range(2,my_num) if calc_prime(x) == True]

def want_to(my_list, my_div):
    """returns yes or no depending of if num in my_list divisible by my_div
    Args: my_num: int
    """
    return ['Yes' if x % my_div == 0 else 'No' for x in my_list]

def ending_letter(my_list,end_str):
    """ returns only strings in <my_list> that end in <end_str>
    Args: my_list: list, end_str: string
    """
    return [x for x in my_list if x[-1] == end_str]

def contains_substring(my_list, sub_str):
    """ returns index of item from <my_list> that contains <sub_str>
    my_list: list of strings, sub_str: strings
    """
    return [my_list.index(x) for x in my_list if x.find(sub_str)>=0]
    """ case insensitive
    return [my_list.index(x) for x in my_list if x.lower().find(sub_str.lower())>=0]
    """

def tax_bill(my_rates, my_income):
    """
    """

     #add the lower bound to rates
    my_rates2 = my_rates
    my_rates2.insert(0,(0,0))
    new_rates = [(x[0],y[0],y[1]) for x,y in zip(my_rates2[:-1],my_rates2[1:])] #zip together new list of rates to inclue upper and lower bound plus rate

    return sum([((x[1] if my_income>x[1] else my_income)  -x[0]) * x[2] for x in new_rates if my_income >= x[0]])   #gets list of rates income applies to based on lower bound, then determines amount to be taxed at that rate (depending on upper bound) and sums the total


def tax_bill_sort(my_rates, my_income):
    """
    """

    my_rates2 = sorted(my_rates) #use internally scoped varible
    my_rates2.insert(0,(0,0)) #add the lower bound to rates
    new_rates = [(x[0],y[0],y[1]) for x,y in zip(my_rates2[:-1],my_rates2[1:])] #zip together new list of rates to inclue upper and lower bound plus rate

    return sum([((x[1] if my_income>x[1] else my_income)  -x[0]) * x[2] for x in new_rates if my_income >= x[0]])   #gets list of rates income applies to based on lower bound, then determines amount to be taxed at that rate (depending on upper bound) and sums the total
