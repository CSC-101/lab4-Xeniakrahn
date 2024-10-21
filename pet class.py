

class Pet:
    def __init__(self,name:str,animal_type: str, age: int ):
        set.__name= name
        set.__animal_type= animal_type
        set.__age= age

    def getname(self) -> str:
        return self.__name
    def getage(self):
        return self.__age
    def getanimal_type(self):
        return self.__animal_type
    def setname(self, name:str)-> None:
        self.__name= name
    def setage(self, age:int):
        self.__age=age
    def setanimal_type(self, animal_type:str):
        self.setanimal_type = animal_type

    def __str__(self):
        return ("Name; {}, Animal Type; {}, Pet Age; {}"
                .format (self.__name, self.__animal_type, self.__age, ))
def main():
    x=input("enter the name of pet")
    y=input("enter the type of pet")
    z=input("enter the age of pet")
    pet1=Pet(x, y, z)
    return()
main()