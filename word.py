def word(st):
    mylist=[]
    str1=""
    mylist=st.split()
    for i in range(len(mylist)-1,0,-1):
        for n in range(i):
            if mylist[n]>mylist[n+1]:
                temp=mylist[n]
                mylist[n]=mylist[n+1]
                mylist[n+1]=temp
    f=1
    j=0
    flag=0
    mylist.append(" ")
    for i in range(len(mylist)-1):
        if mylist[j]==mylist[f]:
            flag+=1
            j+=1
            f+=1
        else:
            print mylist[i]+" : ",
            print flag+1
            flag=0
            j+=1
            f+=1
