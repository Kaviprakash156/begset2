k=int(input("Enter the number:"))
temp=k
rev=0
while(k>0):
    dig=k%10
    rev=rev*10+dig
    k=k//10
if(temp==rev):
    print("Is it a polindrome number?\n","YES")
else:
    print("Is it a polindrome number?\n","NO")
