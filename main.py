def fact1(n):
   if (n==0 or n==1):
     return 1
   else:
     return n*fact1(n-1)
num=int(input("enter a no"))
res=fact1(num)
print("The factorial {}is {}".format(num,res))