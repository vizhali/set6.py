vizh,pop=map(int,input().split())
count1=0
arr=list(map(int,input().split()))[:vizh]
for j in arr:
  if j==pop:
    count1+=1
if(count1!=0):
  print("yes")
else:
  print("no")
