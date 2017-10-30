import numpy as np

def normalize(_array):
    """Write a function that takes in a one-dimensional numpy array and normalizes it (i.e. subtracts off the mean and divides by the standard deviation). Return the normalized array
    Args: _array: numby array
    """
    return [(x-_array.mean())/_array.std() for x in _array]

def normalize2(_array):
    """Now create a version of 1 that takes in a two-dimensional numpy array and normalizes it along the columns (i.e. for each column subtract off its mean and divide by its standard deviation). Return the normalized array.
    Args: _array: 2 column numby array
    """


    return (_array * _array.mean(axis=0) )/_array.std(axis=0)

def create_array(num_cols, num_rows, fill_value):
    """Write a function that creates a numpy array of an inputted shape, filled with an inputted number. Your function should have three parameters - num_cols, num_rows, and fill_value. As an example, if I called your function with num_cols=4, num_rows=3, and fill_value=2, then your function should output a 3 by 4 array of 2s. Return the newly created array.
    """
    return np.zeros(shape=(num_rows,num_cols)) + fill_value
    # np.full((num_rows,num_cols),fill_value)

def array_arith(my_arr, my_int, my_op):
    """Write a function that takes in a one-dimensional numpy array, an int, and a mathematical operator (either +, -, /, or *) as a string, and then performs the indicated operation on each element of the array, using the inputted int. For example, if I inputted a numpy array, 2, and '*', you should multiply each element of the array by 2. If I inputted a numpy array, 5, and '-', then you should subtract 5 from every element in the array. Return the resulting array.
    """
    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x - y), "*": (lambda x,y: x * y), "/": (lambda x,y: x / y), "**": (lambda x,y: x ** y)}
    return ops[my_op](my_arr,my_int)

def randoms(num_elements):
    """Write a function that takes in one argument, an int, and creates a one-dimensional array that is the inputted number of elements long. Make the one-dimensional array full of random floating point numbers between 0 and 1 (Hint: Check out numpy.random.random()). Return the resulting array.
    """
    return np.random.rand(num_elements)

def randoms_shaped(num_elements,num_rows, num_cols):
    """Now, alter your solution to 5 to take in two parameters that will denote the final shape of your array of random floating point numbers (so now you will potentially end up with a two-dimensional array). Name these parameters num_rows and num_cols. Return the resulting array.
    """
    return np.random.rand(num_elements).reshape(num_rows,num_cols)

def random_sample(my_array,num_samples):
    """Write a function that will take in a one-dimensional numpy array, as well as an int, and randomly sample the inputted integer number of elements from the inputted array (Hint: Check out numpy.random.choice()). Return the randomly sampled elements.
    """
    return np.random.choice(my_array,num_samples)

def replace_max(my_array):
    """Write a function that will take in a one-dimensional numpy array and replace the maximum element in it with a 0. Return the resulting array.
    """
    my_array[my_array.argmax()] = 0
    return my_array

def sum_to(max_int):
    """Write a function that takes in an int, creates a one-dimensional numpy array of the numbers from 0 up to int, and then returns the cumulative sum of all those numbers."""
    return sum(np.arange(max_int))

def dot_product(ar, ar2):
    """Write a function that takes in two two-dimensional numpy arrays and performs matrix multiplication, the dot product, between the two. You should construct it such that the first array is multiplied by the second (i.e. the number of columns of the first has to equal the number of rows of the second; you can assume that your inputs will meet this criteria). Return the result of the multiplication."""
    return sum(ar*ar2.transpose())

def el_multiply(ar, ar2):
    """Write a function that takes in two two-dimensional numpy arrays and performs element-wise multiplication between the two. You can assume that the two arrays are of the same size. Return the array resulting from the multiplication."""
    #??? is element-wise supposed to multiply elements at same index independent of the shape?  if so this won't work
    #ar*ar2 should work
    return np.multiply(ar,ar2)

def top_five(ar):
    """Write a function that takes in a one-dimensional numpy array and returns the top 5 elements (you can assume it's an array of numbers)."""
    # return ar[np.argpartition(ar,1)[-5:]] # supposed to be faster than full sort
    return ar[(-ar).argsort()[:5]]

def top_five2(ar):
    """Write a function that takes in a two-dimensional numpy array and returns the smallest 5 elements of each column (Hint: The axis parameter on the numpy function you use might come in handy here)."""
    return np.partition(ar,2, axis = 1)[:,:5]


def ec(max_int):
    """
    """
    a_size = int(np.sqrt(max_int))
    return sum(np.mean(np.arange(max_int)[:a_size**2].reshape(a_size,a_size),axis=1))
