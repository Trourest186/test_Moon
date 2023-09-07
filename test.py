grades=[]
while True:
    grade = input("Input:")
    if grade == "-1":
        break
    grades.append(grade)

print(grades)

print("\nContinue\n")

tb = int(sum(grades) / len(grades))

print(tb)