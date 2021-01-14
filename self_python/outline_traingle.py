n=int(input("enter num"))
for i in range(0,n):#0 in(0,6)-t,
    if i==0:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"*1 +" "*(2*(i-1)+1)+"*"*1)#6-1
for i in range(n,-1,-1):#0 in(0,6)-t,
    if i==0:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"*1 +" "*(2*(i-1)+1)+"*"*1)#6-1