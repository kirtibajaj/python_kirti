num=int(input("Enter a number:"))
s=0
n=num
x=0
while(n):
    n=n//10
    x+=1
n=num
while(n):
	r=n%10
	s=s+pow(r,x)
	n=n//10
if s==num:
	print("Armstrong")
else:
	print("Not Armstrong")
