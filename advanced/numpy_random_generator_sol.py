"""
Task: 
Create a random generator `np_rand` function that generates 10 random numbers between 0 and 10.

The inputs should be a string argument denoting the type of random number ("float" or "int") to get and a seed (int).

The function should return a numpy array of random numbers. 

Then create a program which prompts the user for a data type (float or int) and seed and prints the result of `np_rand` with the given seed and data type.
"""

import numpy as np

def np_rand(data_type, seed = None):
    if seed is not None:
        np.random.seed(seed)
        
    if data_type == "float":
        return np.random.uniform(0, 10, 10)
        # other possible solutions
        # return np.random.random(10) * 10
        # return np.random.rand(10) * 10
    elif data_type == "int":
        return np.random.randint(0, 10, 10)
    else:
        raise ValueError("data_type must be either 'float' or 'int'")
    

data_type = input("Enter data type (float or int): ")
seed = int(input("Enter seed: "))
print(np_rand(data_type, seed))