#to print number from 0 to 9
for i in range(10):
  print(i)

#to print in steps
for i in range(1,10,2):
  print(i)

#to print strings
str="priya sah"
for i in str:
  print(i)

##While loop
#print 5 numbers 
count=0
while count<5:
  count=count+1

##break statement
for i in range(6):
  if(i==5):
    break
    print(i)

##Continue statement
for i in range(10):
  if(i==5):
    continue
  print(i)


##Pass statement
for i in range(5):
  if i==3:
    pass
    print(i)

#nested loop
for i in range(5):
    for j in range(2):
        print(f"i:{i}and j:{j}")

##Sum of first n natural number
num=10
sum=0
count=1
while count<=num:
    sum=sum+count
    count+=1
print(sum,"is sum of first 10 natural number")


