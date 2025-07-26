def total(marks_list):
    return sum(marks_list) 
    
def avg(marks_list):
    return sum(marks_list)/ len(marks_list)
    
def grade(average):
    if average>=90 and average<=100:
        return "A"
    elif average>=80 and average<=89:
        return "B"
    elif average>=70 and average<=79:
        return "C"
    elif average>=60 and average<=69:
        return "D"
    elif average<60:
        return "F"
    else:
        return "Invalid Marks"

all_students=[]
        
num_students=int(input("Num of Students:"))
for f in range(1,num_students+1):
    stu_name=input("Enter Name of Student:")
    
    subjects=int(input("Num of Subjects:"))

    marks_list=[]
    for i in range (1,subjects+1):
        marks=int(input(f"Enter the Marks of subject {i}:"))
        marks_list.append(marks)
    
    total=total(marks_list)

    average=avg(marks_list)
    
    stu_grade=grade(average)

    student_report={
        "name":stu_name,
        "marks":marks_list,
        "total":total,
        "average":average,
        "grade":stu_grade
    }
    all_students.append(student_report)

    print("----- Report Card -----")
    print("Name: ",student_report["name"])
    print("Marks per Subject",student_report["marks"])
    print("Total Marks:",student_report["total"])
    print("Average:",student_report["average"])
    print("Grade:",student_report["grade"])