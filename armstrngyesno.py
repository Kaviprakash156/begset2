num=int(input("enter the number:\n"))
print("Is this an Armstrong number?\n")
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"\nYES,this is an Armstrong number")
else:
   print(num,"\nNO,this is not an Armstrong number")
