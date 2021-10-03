import json
from school import Student




def main():
    students = []
    with open('students.json') as json_data:
        jsonStudents = json.load(json_data)
        for jsonStudent in jsonStudents:
            student = Student(jsonStudent['id'], jsonStudent['name'], jsonStudent['age'], jsonStudent['attendance'])
            students.append(student)

    print('-----------------------------------------------')
    youngestIndex = 0
    youngest = students[youngestIndex].name
    for i in range(1,len(students)):
        if (students[i].age < students[youngestIndex].age):
            youngestIndex = i
            youngest = students[youngestIndex].name

    print(f'Youngest: {youngest}')
    print('-------------------------------------------------')


    oldestIndex = 0
    oldest= students[0].name
    for i in range(1, len(students)):
        if (students[i].age > students[oldestIndex].age):
            oldestIndex = i
            oldest = students[oldestIndex].name
    print(f'Oldest: {oldest}')

    print('--------------------------------------------------')
    count = 0
    average = 0

    for i in range(0,len(students)):
        count += students[i].age
    average = int(count/len(students))
    print(f'Average age: {average}')
    print('------------------------------------------------')
    studentAttendce = []

    for i in range(0,len(students)):
        if students[i].attendance < 30:
            studentAttendce.append(students[i].name)
    for k in studentAttendce:
        print(f'Bad student: {k}')




if __name__ == '__main__':
    main()
