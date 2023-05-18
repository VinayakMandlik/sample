
#Assignments

#1. Write program to accept two numbers from user and use divide function to divide two numbers. Implement 
# exception handling to check it divisor is ZERO.

try:
    a=int(input("Enter a:"))
    b=int(input("enter b:"))
    print(a/b)
except:
    print("zero division error")
else:
    print("Done")



#2. Accept age, height, weight,name and surname for user.age should be an integer, height and weight should be 
#floats, and name and surname should be strings.If the user enters input of the incorrect type, keep prompting 
#the user for the same value until it is entered sorrectly. Give the user sensible feedback.

while(1):
    try:
        age=int(input("age:"))
        ht=float(input("HEight:"))
        wt=float(input("Weight:"))
        name=input("Name:")
        surname=input("Surname:")
    except:
        print("Incorrect input")
    else:
        print("DOne")
        break


#3. Add a try-except statement to the body of this function which handles a possible IndexError, which could 
#occur if the index provided exceeds the length of the list. Print an error message if this happens
#: def print_list_element(thelist, index): print(thelist[index])

def print_list_element(thelist, index):
    return print(thelist[index])
try:
    thelist=[10,20,30,40,50,60]
    index=int(input("Index:"))
    print_list_element(thelist,index)
    
except IndexError:
    print("Index exceeds the list lenght")
    


#4. This function adds an element to a list inside a dict of lists. Rewrite it to use a try-except statement which
#handles a possible KeyError if the list with the name provided doesn't exist in the dictionary. Include else and
#finally clauses in your try-except block:
class KeyNotInListException(Exception):
    pass
def add_to_list_in_dict(thedict, listname, element): 
    try:
        key = thedict.keys()
        if listname not in key:
            raise KeyNotInListException()
    except KeyNotInListException as e:
        thedict.update({listname:element})
    else:
        print(listname,thedict[listname])
    finally:
        print(thedict)
            
thedict = { 'names' : ['Harshal, Vedant, Akshay'], 'roll_nos' : [10, 5, 12]}
listname = input('Enter listname: ')
elements = ['Amrutkar', 'Bhosale', 'Funde']
add_to_list_in_dict(thedict,listname, elements)        
    
#5. Write a program to accept age from user and check if user age is valid for voting or not. raise
#invalidageException if user enter <18 value, also handle all possible exceptions.
while(1):
    try:
        age=int(input("Enter age:"))
        if age<18:
            raise Exception ("You are not eligible for voting")
        else:
            print("You are eligible for voting!")
    except Exception as e:
        print("Wrong input,Enter valid age ",e)
    else:
        print("Done")
        break


#6. Write program to accept,display list of numbers, use SearchByPosition function to search element from fist by
# position accept pos and element from user), check following things.
#1. Check if position is grater then list size. (raise exception)
#2. if element is not available. (raise exception)
#3.You have to catch all the raise exceptions also.

def SearchByPosition(l):
    try:
        no=int(input("Enter 1 to search by poistion || enter 2 to search by element"))
        
        if no==1:
            i=int(input("Enter index"))
            if i>=len(l):
                raise Exception ("Index out of bound")
            else:
                print(l[i])
        if no==2:
            element=int(input("Enter element to search :"))
            if element in l:
                print(element,"is present in list")
            else:
                raise Exception ("Elemennt is not present")
    except Exception as e:
        print(e)

l=[1,2,3,4,5,6,7,8,9,10]
print(SearchByPosition(l))
                
            
        
            
        
        
        





















