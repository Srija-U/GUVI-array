 n=int(input())
l=[int(i) for i in input().split()]
l.sort(reverse=True)
print(*l,sep='')
