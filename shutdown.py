user=input("enter your answer y/n")
def shutdown(user):
    if user=='y':
        print("shutting down")
    elif user == 'n'  :
       print("abort shutting down")  
    else:
        print("sorry")   