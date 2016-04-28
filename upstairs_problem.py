# coding=utf-8 
def upstairs(n): 
   if n==1: 
       return 1 
   elif n==2:
       return 2 
   else : 
       return(upstairs(n-1)+upstairs(n-2)) 
num=input()  
print(upstairs(int(num))) 
