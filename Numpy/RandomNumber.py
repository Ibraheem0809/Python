import numpy as np

# rng is an object that we can use in our whole code
rng = np.random.default_rng() # seed=1 can be used to reproduse same result

print(rng.integers(low=0,high=10,size=(2,2))) # from size we can create a 2D array as well


# for boolean

print(np.random.uniform(low=-1,high=1,size=3))

# suffle array

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# random choice

fruits = np.array(["🫐", "🥑", "🥭", "🍓", "🥝"])
fruitx = rng.choice(fruits,size=3)
print(fruitx)