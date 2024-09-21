class person:
    name=""
    age="0"
    gender=""

    def __init__ (self,personName,personage,persongender):
        self.name=personName
        self.age=personage
        self.gender=persongender
    def talk(self):
        print("hi")


# username=input("please enter name:")
# userage=input("please enter age:")
# usergendere=input("please enter gender:")
# person1=person(username,userage,usergendere)
# print(person1.name)
# person1.talk()

yamen=person("yamen", "13","male")

print(yamen.gender)