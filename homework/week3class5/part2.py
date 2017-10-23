#1
def any_beers(n=0):
    """any of them beers left?
    Args: n: int
    """
    if n > 0:
        return 'Beers left!'
    else:
        return "Ain't no beers left!  Hit the store yo!"
def true_fans(name):
    """check if a person is a true Elsa fan, all others get cold shoulder
    Args: name: string
    """
    true_fans = set('Cary','Josh','Sean')
    if name in true_fans:
        return True
    else:
        return False

def calc_sum(my_list):
    """sum up those numbers
    Args: my_list: list
            sum_total: float
    """
    sum_total = 0
    for x in my_list:
        sum_total += x
    return sum_total

def calc_product(my_list):
    """product up those numbers
    Args: my_list: list
            product_total: float
    """
    product_total = 1
    for x in my_list:
        product_total *= x
    return product_total


def calc_even(my_list):
    """return even number from list
    Args: my_list: list

    """
    return [x for x in my_list if x % 2 == 0]
