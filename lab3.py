from dataclasses import dataclass
"""
Part 3: Student dataclass
Type in the dataclass code from the slides/video
Add one more field: gpa, a float
Write a main function to create some example Student objects with some example names, college_id and GPA values. 
Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 
Add some comments in your code to compare the dataclass version to the "traditional" version
"""


# it looks to me like the the decorator reduces boilerplate code. The init and self syntax can be a bit annoying to right
# especially for class function definitions (self, somevar, somevar2)
@dataclass
class Student:
    name: str
    college_id: int
    gpa: float
    
def main():
    alice = Student('alice', 12345, 3.5)
    bob = Student('bob', 6789, 2.2)
    chris = Student('chris', 6789, 2.2)
    print(alice)
    print(bob)
    chris.gpa = 10
    print(chris)
    print(chris.gpa)

main()