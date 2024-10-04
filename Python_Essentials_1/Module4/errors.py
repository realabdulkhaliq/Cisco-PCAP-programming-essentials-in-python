# What is the output of the following program if the user enters 0?

try:
    value = int(input("Enter a value: "))
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except:
    print("Booo!")
    

# The program will output: Very bad input....