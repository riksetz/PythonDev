''' 
def main():
    print ("CSE1PE Week 1: Python Lab")
    person_name = input('Enter person name: ')
    person_age = input(int('Enter person age: '))
    if person_age == 1:
        print ('Baby ' + person_name + ' is 1 year old.')
    elif person_age < 5:
        print ('Todler is ' + person_age + ' years old.')
    else:
        print (person_name + ' is ' + person_age + ' years old.')
#This is a comment. First failed program lol, fix later.
'''
print ("\nCSE1PE Week 1: Python Lab \n")
person_name = input('Enter person name: ')
person_age = input('Enter person age: ')
if person_age == '1':
    print ('Baby ' + person_name + ' is 1 year old.')
else:
    print (person_name + ' is ' + person_age + ' years old.')
