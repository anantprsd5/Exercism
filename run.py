def run_length(n):
    result = []
    flag=0
    f=1
    i=0
    n=n+" "
    new=""
    for j in range(len(n)-1):
        if n[i] == n[f]:
            flag+=1
            i+=1
            f+=1
        else:
            result.append(str(flag+1))
            result.append(n[j])
            flag=0
            i+=1
            f+=1
    for i in result:
        new=new+i
    return new

