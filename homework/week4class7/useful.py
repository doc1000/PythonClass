
#(sum(x) for x in range(1,1000))

#sum(x for x in range(1,1000000))

py_list = range(1000000)
%timeit sum(py_list)

np_arr = np.arange(1000000)
%timeit np.sum(py_list)

SIMD - look it up on wikipedia
use NumPy for most math operations - way faster - get used to it.

initiate NumPy arrangs from python lists and tuples
determine NumPy data type and shaep of an arraysmix andx taypecasts data in an array
make a 2D array (matrix) wit a list of lists (but realize that matrix is a special type in NumPy)


alpha = np.array([1.,2.,3.,4.,5.])
alpha.shape
alpha.dtype
bravo = np.array((1,2,3,4,5,6,7),np.int64)
bravo.shape
bravo.dtype


alpha = np.array([1.,2.,3.,4.,5.]).reshape(-1,1)
alpha = np.array([1.,2.,3.,4.,5.]).reshape(1,-1)

 np.arange(-10,1).reshape(3,3).T
 np.linspace(0.,100.,5).reshape(-1,1)



 np.random.rand(3,3).flatten().reshape(1,-1).shape

 Broadcasting ans Element-Wise operations
