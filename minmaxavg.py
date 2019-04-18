k=int(input("enter the value"))
l=[]
for i in range(k):
     m=int(input("enter the elements"))
     l.append(m)
a=sum(l)

avg=float(a//k)
print(avg)
print(min(l))
print(max(l))
