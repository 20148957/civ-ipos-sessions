# a basic import
from src.greeter import greet as gt
from src.Student import *

# use an alias - consider why might we do this?
def main():
    gt()
    student = Student('Albie', '20148957', [1, 2, 5], 'Nowhere')
    print(student.id)
    student.setId(1)
    print(student.id)
# sometimes we only want to import what we need

# create a calculator class in the module

# use the new class to return a score to a user


if __name__ == '__main__':
    main()