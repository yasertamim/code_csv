from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import time


Base = declarative_base()


student_course_table = Table('student_course', Base.metadata,
                             Column('course_id', ForeignKey('courses.id')),
                             Column('student_id',ForeignKey('students.id')))

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    year = Column(Integer)
    courses = relationship("Courses", secondary=student_course_table, back_populates='students')

class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_students = Column(Integer)
    tests = relationship("Tests", back_populates= "course")
    students= relationship("Students", secondary=student_course_table, back_populates='courses')

class Tests(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_time = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Courses", back_populates="tests")




def main():
    print('1.Add student')
    print('2.Add course')
    print('3.Add test')
    print('4.Add student to course')
    print('5.List courses by student')
    print('6.List tests by course')
    print('7. Exit')

    choice = int(input('enter a choice'))
    engine = create_engine('sqlite:///school.sqlite')
    Session = sessionmaker(bind=engine)

    session = Session()

    if choice == 1:
        name = input('enter the name of student ')
        email = input('enter the email')
        year = int(input('enter the year'))
        new_student = Students(name= name, email= email, year= year)
        session.add(new_student)
        session.commit()
        print(f'Added student with id {new_student.id}')
    elif choice == 2:
        name = input('enter the course name')
        max = int(input('enter the max students'))
        new_course = Courses(name=name, max_students=max)
        result= session.add(new_course)
        session.commit()
        crs = session.query(Courses).filter(Courses.name == name)
        print(f'Added course with id {new_course.id}')
    elif choice == 3:
        course_id = input('enter the course id')
        name = input('enter the test name')
        date = str(input('enter the date and time'))

        new_test = Tests(course_id= course_id, name=name, date_time=date)
        session.add(new_test)
        session.commit()
        print(f'Added test with id {new_test.id}')
    elif choice == 4:
        std_id = int(input('enter the student id'))
        crs_id = int(input('enter the course id'))
        result = session.query(Students).get(std_id)
        result1 = session.query(Courses).get(crs_id)
        #res = session.query()
        if result and result1:
            #new_student = Students(id =result.id ,name=result.name, email=result.email, year=result.year)
            result1.students.append(result)
            session.commit()
            print(f'Added student to course id {crs_id}')
        elif not result:
            print(' Student not found')
        elif not result1:
            print('Course not found')



    elif choice == 5:
        std_id= int(input('enter the student id'))
        result = session.query(Students).get(std_id)

        if result:

            print(f'Courses for student {std_id}:', end=' ')
            for i in result.courses:
                print(i.name, end=', ')
        elif not result:
            print("Student not found")



    elif choice == 6:
        cors_id = int(input('enter the course id'))
        result = session.query(Courses).get(cors_id)
        if result:
            test = session.query(Courses.tests).all()

            print(f'Tests for course {cors_id}:', end=' ')
            for i in result.tests:
                print(i.name, end=', ')

    elif choice == 7:
        exit()




if __name__ == '__main__':
    main()
