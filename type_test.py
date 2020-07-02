# if the code was intended to be python 2, then you should run "mypy --py2 type_test.py"
# otherwise, you can omit the --py2

from typing import List, NewType
from uuid import uuid4, UUID

# This line defines a new type that can be used by the type checker to enforce expected behavior across the codebase.
# In this case, it prevents you from confusing normal strings with UUID strings.
UUIDString = NewType('UUIDString', str)

def new_uuid():
    # type: () -> UUID
    return uuid4()

def new_uuid_str(uid):
    # type: (UUID) -> UUIDString
    return UUIDString(str(uid))

class Person:
    def __init__(self, id, first_name, last_name):
        # type: (UUIDString, str, str) -> None
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

def say_hello(person):
    # type: (Person) -> None
    print('{0}: {1} {2} says "Hello there!"'.format(person.id, person.first_name, person.last_name))

uu = new_uuid() # type: UUID
uust = new_uuid_str(uu) # type: UUIDString

# this is the expected type
harry_potter = Person(id=uust, first_name='Harry', last_name='Potter') # type: Person

# comment out the above line, and uncomment the bolow line to see the type checker working
# harry_potter = Person(id=str(uu), first_name='Harry', last_name='Potter') # type: Person

say_hello(harry_potter)
