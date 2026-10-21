list = [2,3,4,-5,6,7]
count =0
sum = 0
for i in list:
    count+=1
    if( i > 0):
        sum += i
        # continue

print("total marks:",sum)
print("total student:",count)