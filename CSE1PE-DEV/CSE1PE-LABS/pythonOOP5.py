# Cretate the class (program template)
class PartyPeople:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print (self.name, "constructed")
    def party (self):
        self.x = self.x + 1
        print (self.name, "party count", self.x)
# Inheritance
class FootballFan(PartyPeople):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        # Calls adds 1 again to party count.
        self.party()
        print (self.name, "points", self.points)
        
s = PartyPeople("Rick")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

#     # Create methods/function class has
#     # Constructor
#     def __init__(people):
#         print ("I am constructed.")
#     # Created Method
#     def party(people):
#         people.x = people.x + 1
#         print ("So far",people.x)
#     # Destructor
#     def __del__(people):
#         print ("I am destructed",people.x)
           
# # Construction - Object created in class
# call = PartyPeople()
# # 'Call' is an alias for 'people'
# call.party()
# call.party()
# print ("Call contains", call)
# # Over-ride call
# call = 42
# print ("Call contains", call)

# y = "\nHello World"
# y_function = dir(y)
# y_type = type(y)

# print (f"{y} belongs to {y_type} and has the following capabilities:\n{y_function}")
# print (y)
# print (y.lower())
# print (y.upper())
# print ("yes".upper())

# PartyPeopleType = type(PartyPeople)
# PartyPeopleFunction = dir(PartyPeople)
# print (f"PartyPeople() belongs to {PartyPeopleType} and has the following capabilities:\n{PartyPeopleFunction}")





    