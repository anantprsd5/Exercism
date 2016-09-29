def diff():
    arr=[]
    s=0
    s1=0
    n=input("Enter the value of n")
    for i in range(n):
        val=input("enter " + str(i+1) + " Value")
        arr.append(val)
    for i in arr:
        s=s+i**2
        s1=s1+i
    diff=s1**2-s
    return diff
