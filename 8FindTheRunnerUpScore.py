if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # NOTE: limit the input as much as n
    newarr=[]
    i=0
    for a in arr:
        i=i+1
        if i<=n:
            newarr.append(a)

    mx=max(newarr)
    a=[]
    for x in newarr:
        if x<mx:
            a.append(x)
    print(max(a))
