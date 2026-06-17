import numpy as np

digit = int(input("Enter number of digits: "))

OTP = np.random.randint(10**(digit-1),10**digit)

print("OTP: ",OTP)

# np.random.randint(low, high) generates a random integer in that range.