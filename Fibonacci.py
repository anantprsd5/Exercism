def fibonacci(n):
    a=1
    b=0
    c=0
    while(c<n):
        c=a+b
        if(c<10):
            print(c)
            a=b
            b=c
