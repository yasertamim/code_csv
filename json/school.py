class Student:
  def __init__(self, id, name, age, attendance):
    self.id = id
    self.name = name
    self.age = age
    self.attendance = attendance

  def printStudent(self):
    print("Student: " + str(self.id) + ", " + str(self.name) + ", " + str(self.age) + ", " + str(self.attendance))
