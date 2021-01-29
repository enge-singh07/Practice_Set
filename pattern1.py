# def pypart(n): 
#     for i in range(0, n): 
#         for j in range(0, i+1): 
#           print("* ",end="")  
#         print("\r") 
# n = 5
# pypart(n) 

# Python 3.x code to demonstrate star pattern 
  
# Function to demonstrate printing pattern 
def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
        myList.append("*"*i) 
    print("\n".join(myList))  
# Driver Code 
n = 5
pypart(n)