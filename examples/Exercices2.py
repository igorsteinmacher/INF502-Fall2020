total=0
count=0

list_numbers=[2,6,2,5,8,2,7,3,5,3,5,7]
for element in list_numbers:
    total += float(element)
    count += 1
    average = total / count

print ('count',count,'sum',total, 'avg',average)

