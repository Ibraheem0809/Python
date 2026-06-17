"""

try
 └── Code that may fail

except
 └── Handles the error

else
 └── Runs if no error occurs

finally
 └── Always runs

"""


try:
    num = int(input("Enter any number:"))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot Divided by Zero")
except ValueError:
    print("Enter a valid Number")
