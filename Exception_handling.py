x = int(input("enter a number :"))
try:
    print(5/x)
except ZeroDivisionError as e:
    print(e)

print("remainig code")

# To handle all type of error :
x = int(input("enter a number :"))
try:
    print(5/x)
except Exception as e: # To handle any type of error.
    print(e)

print("remainig code")

# Finally error handling
x = int(input("enter a number :"))
try:
    print(5/x)
finally:
    print("Finally handled")

