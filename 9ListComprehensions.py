if __name__=='__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    n=int(input())

    xx=[xi for xi in range(x+1)]
    yy=[yi for yi in range(y+1)]
    zz=[zi for zi in range(z+1)]
    #print(xx)
    #print(yy)
    #print(zz)

    #ll=[o for o in range(0,100+1)]
    #print(ll)

    mylist=[]
    for i in xx:
        for j in yy:
            for k in zz:
                if i+j+k!=n:
                    mylist.append([i,j,k])

    print(mylist)
