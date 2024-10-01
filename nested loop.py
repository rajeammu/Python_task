# In 5 row and column to print number 1-25
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j:2}",end='  ')
    print()
#To print 1 in first row ,2 in second row and goes on
for i in range(1,6):
    for j in range(1,6):
        print(i,end="  ")
    print()
    
#To print 1 in first row ,2 in second row and goes on in reverse order
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i, end="  ")
    print() 
#To print star pattern in 5 row and 5 column
star = 5
for i in range(star):
    for j in range(star):
        print('*',end = "  ") 
    print()
#To print 0 in one row and 1 in one row
size=5
for i in range(size):
    for j in range(size):
        if i%2==0:
         print("0",end=" ")
        else:
            print("1",end=" ")
    print() 
#To print 010101    
size=5
for i in range(size):
    for j in range(size):
        if j%2==0:
         print("0",end=" ")
        else:
            print("1",end=" ")
    print()
#To print ABABAB    
size=5
for i in range(size):
    for j in range(size):
        if j%2==0:
         print("A",end=" ")
        else:
            print("B",end=" ")
    print()    
#To print A in one row and B in one row
size=5
for i in range(size):
    for j in range(size):
        if i%2==0:
         print("A",end=" ")
        else:
            print("B",end=" ")
    print() 
 # Number of  * rows increasing in the pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
 # Number of  * rows increasing in the pattern
# Define the number of rows
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
 

                                       
    
    