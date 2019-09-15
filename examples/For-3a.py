grades = [["John",60],["Paul", 84], ["Ben", 70], ["Tony",35]]
for entry in grades:
    if (entry[1]>60):
        print(entry[0] + ": approved")
    else:
        print(entry[0] + ": talk to the instructor")

