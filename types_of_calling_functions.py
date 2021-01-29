import sys
sys.path.append(r"F:\python\python course with notes\8. Chapter 8")
# Types of fuction calling
#1st type
import factorial_04 as sumit
a=sumit.factorial_iter(5)
print(a)
#2nd type
from factorial_04 import factorial_iter
a=factorial_iter(5)
print(a)
#3rd type
import factorial_04
factorial_04.factorial_iter
factorial_04.factorial_recursive
#4th type 
# from factorial_04 import from factorial_04 *
# factorial_iter
