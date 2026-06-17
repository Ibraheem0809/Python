import numpy as np

# dimensions of array { arr.ndim}

arr = np.array("A")
print(arr.ndim)
print(arr.shape)

arr2 = np.array(["A","B","C"])
print(arr2.ndim)
print(arr2.shape)

arr3 = np.array([
    ["A","B","C"],
    ["D","E","F"]
])
print(arr3.ndim)
print(arr3.shape)

arr4 = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
[["J","K","L"],["M","N","O"],["P","Q","R"]],
[["S","T","U"],["V","W","X"],["Y","Z","&"]]])
print(arr4.ndim)
print(arr4.shape)
print(arr4)