# student grade program using the input filed

marks = int(input(" Enter the student marks"))
print(marks)

if marks >=70 and marks<=100:
    print("Grade A")
elif marks >= 60 and marks <= 69:
    print("Grade B")
elif marks >= 35 and marks <= 59:
    print("Grade C")
else:
    print("Student Fail")
