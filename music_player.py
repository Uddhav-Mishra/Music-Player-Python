import os
from os import listdir
from os.path import isfile, join
a = [f for f in listdir("C:/Users/ABC/Videos") if isfile(join("C:/Users/ABC/Videos", f))]
print(a)
s=input("enter song")
i = 1000;j=1000
m = [[0 for x in range(j)] for y in range(i)]
b = [0 for x in range(j)]
for i in range(len(a)):
    z = a[i]
    y = 0
    for j in range(0,1000):
        for k in range(0,1000):
            m[j][k]=0;
    print("here\n")
    for j in range(0, len(a[i])+1):
        for k in range(0, len(s)+1):
           if (j==0 or k==0):
               m[j][k]=0
           elif (a[i][j-1]==s[k-1]):
               m[j][k]=m[j-1][k-1]+1
           else:
               m[j][k]=max(m[j-1][k],m[j][k-1])

    for j in range(0, len(a[i])):
        for k in range(0, len(s)):
            print(m[j][k],end=' ')
        print("\n")

    #print(len(a[i]),len(s),"len  ",m[len(a[i])+1][(len(s))+1])
    if (len(s)==m[len(a[i])][(len(s))]):
        print("start bitch")
        os.startfile(os.path.normpath("C:/Users/ABC/Videos/"+a[i]))
        break;


