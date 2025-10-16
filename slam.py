import sys

def initial_phonebook():
    rows, cols = int(input("Please add your initial number of contacts :")),5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
        print("NOTE: * indicates mandatory fiels")
        print("............................................................")
        temp = []
        for j in range(cols):
            if j== 0:
                temp.append(str(input("Enter name*:")))
                if temp[j]  == ' ' or temp[j]=='':
                    sys.exit("name is a mandatory fielld.process exiting due to blank field")
            if j== 1:
                temp.append(int(input("Enter number*:")))  
            if j== 2:
                temp.append(str(input("Enter friends name:")))
                if temp[j]  == ' ' or temp[j]=='':  
                    temp[j]  = None
            if j== 3:
                temp.append(str(input("Enter date of birth*:"))) 
                if temp[j]  == ' ' or temp[j]=='':  
                    temp[j]  = None
            if j== 4:
                temp.append(str(input("Enter date of birth*:"))) 
                if temp[j]  == " " or temp[j]=='':  
                    temp[j]  = None
        phone_book.append(temp)            
    print(phone_book)
    return phone_book

def menu():
    
    print("*************************************************************************")
    print("\t\t\t SMARTPHONE DIRECTORY")
    print("*************************************************************************")
    print("\tyou can now perform the following operations on this phonebook")
    print("1. Add a new friend name.")
    print("2. Remove an existing  friend.")
    print("3.Delete all friends.")
    print("4.Search for an existing friend")
    print("5.Diisplay all friend.")
    print("6 Exit  slam book")

    choice = int(input("please enter your choice"))
    return choice
def add_contact(pb):

    dip = []
    for i in range(len(pb[0])): 
        if i == 0:
            dip.append (str(input("Enter name")))
        if i == 1:
            dip.append  (int(input("enter number")))   

        if i == 2:
            dip.append  (str(input("enter e-mail"))) 
        if i == 3:
            dip.append  (int(input("enter date of birth"))) 
        if i == 4:
            dip.append  (int(input("enter category")))         

    pb.append(dip)

    return pb
def remove_existing(pb):
    query = str(input("please enter the removed contact that you wish"))
    temp = 0
    for i in range(len(pb)):
        if query == 