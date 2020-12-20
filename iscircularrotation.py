
def rightrotate(b):
	a=len(b)
	l3=[]
	i=0
	while i < a:
		l3.append(b[i])			
		i+=1
	print(l3) 		
	i=1
	tmp=l3[a-1]
	while i < a:
		l3[a-i]=l3[a-i-1]			
		i+=1
	l3[0]=tmp
	print(l3)
	s3="".join(l3)
	return s3	

def isrotate(s1,s2):
	L=len(s1)
	i=1
	r=s1
	while i <= L:
		r=rightrotate(r) 
		if r == s2:
			return 1	
		i+=1
	return -1




l1='apple'
l2='laapp'
output=rightrotate(l1)
print(output)

l3='abcdefghijklmnopq'
l4='qabcdefghijklmnopq'



output=isrotate(l1,l2)
print(output)

output=isrotate(l3,l4)
print(output)


