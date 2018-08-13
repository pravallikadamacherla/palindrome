c=int(input())
b=c
rev=0
while c!=0 :
	s=c%10
	rev=(rev*10)+s
	c=c//10
if rev==b:
	print("yes")
else: 
	print("no")
