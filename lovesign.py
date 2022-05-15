import math
n=11
i=1
j=1
y=math.floor(n/2)-1
for i in range(1,n):
    for j in range(1,n+1):
        if (i==1):
            if j==i or j==i+1 or j>=i*(n-1) or j==round(n/2) :
                print(" ",end=" ")
            else:
                print("*",end=" ")
        elif i==2:
            if j==i or j==round(n/2) or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        elif i>=3 and i<=5:
            if j==1 or j==n:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        elif i>5 and i<(n-1):
            x = math.floor((n/2))-1
            if j==i-x or j==i+y:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        elif i==(n-1) and j==round(i/2):
            if j ==round(n / 2):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        elif i==(n-1):
            if j==round(n/2):
                print("*",end="")
            else:
                print(" ",end=" ")
    if(i>5):
        y=y-2
    print("")
