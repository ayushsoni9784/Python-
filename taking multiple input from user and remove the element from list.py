#!/usr/bin/ python



a=[]
n=int(input("Enter the no. of input "))
for i in range(0,n):
    w=int(input())
    a.append(w)
print(a) 
q=int(input("Enter the no to search in the list "))
if q in a :
    a.remove(q)
else :
    print("not found") 
print(a)







