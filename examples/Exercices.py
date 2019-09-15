total = 0
count = 0
average = 0
while True:
    number = input("Enter a number:")
    if number == "done":
        break
    total += float(number)
    count += 1
    average = total / count
print ('count',count,'sum',total, 'avg',average)


