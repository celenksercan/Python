import numpy as np

py_list=[1,2,3,4,5,6,7,8,9]
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))


py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_array.reshape(3,3)

print(py_list)
print(np_array)

# boyutu görme
print(np_array.ndim)
print(np_multi.ndim)