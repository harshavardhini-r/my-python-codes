marks = []

print("Enter marks of 5 subjects:")

for i in range(5):
    m = float(input(f"Enter mark {i+1}: "))
    marks.append(m)

total = sum(marks)
avg = total / len(marks)

print("Total marks:", total)
print("Average:", avg)

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
else:
    print("Grade: D")
