class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass
p, s = Person(), Student()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object)) # object = 뿌리, 근본 <object - UML클래스 - 상속받는클래스>
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))