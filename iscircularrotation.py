
def rightrotate(b):
	a=len(b)
	l3=[]
	l3.append(b[a-1])
	i=0
	while i < a-1:
		l3.append(b[i])			
		i+=1
	s3="".join(l3)
	print(s3)
	return s3	

def isrotate(s1,s2):
	L=len(s1)
	i=1
	r=s1
	while i <  L:
		r=rightrotate(r) 
		if r == s2:
			return 1	
		i+=1
	return -1




l1='apple'
l2='pplea'

l3='abcdefghijklmnopq'
l4='qabcdefghijklmnop'



output=isrotate(l1,l2)
print(output)

output=isrotate(l3,l4)
print(output)


