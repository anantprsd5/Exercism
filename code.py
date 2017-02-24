a,b = raw_input().split(' ')
arr=[]
arr1=[]
arr1.append(a)
arr1.append(b)
n=input()
arr=[]
arr2=[]
arr2.append(a)
arr2.append(b)
j=2
k=0
for i in range(0,n):
	d,e = raw_input().split()
	arr.append(d)
	arr.append(e)
	if(arr[i] == arr1[i]):
		arr1.append(arr[i+1])
		arr1.append(arr1[i+1])
	elif(arr[i]==arr1[i+1]):
		arr.append(arr[i+1])
	arr2.append(arr1[j])
	arr2.append(arr1[j+1])
	j=j+1
print(arr2)

	
	
