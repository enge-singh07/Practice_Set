li[]
for i in range(1,51):
    if(i%3==0 or i%5==0):
        li.append(i)
    print(li)

# List Comprehension
x=[i for i in range(1,51) if (i%3==0 or i%5==0)]
print(x)