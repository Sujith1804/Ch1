def fact (n) :
if n==0 or n==:
return 1 else:
return n*fact (n-1)
num=int (input ("Enter the value:"))
res=fact (num)
print (f"The factorial of (num) is (res)")