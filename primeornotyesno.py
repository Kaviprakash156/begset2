num=int(input("enter the number:\n"))
print("\nIs this prime number?\n")
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("NO,this is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print("YES, this is a prime number")
else:
   print("NO,this is not a prime number")
