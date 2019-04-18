p=int(input(" enter the value"))
for x in range(1,p+1):
     for y in range(2,x):
          if x%y==0:
               break
     else:
          print (x,sep=' ', end=' ')
