import string
import random

start = True
user_data={}
user_id=0
container ={}
 

def get_detail():
    
    user_first_name = input("Please Enter your Fist name here: ")
    user_last_name = input("Please Enter your last name here: ")
    name = user_first_name+" "+ user_last_name
    user_data["Name"] = name
    user_email = input("Please Enter Your email here: ")
    verify_email = check_email(user_email)          

    while verify_email==False:
        print ("The email address you entered is most likely incorrect! Please try again.")
        user_email = input("\nPlease Enter email here: ")
        verify_email = check_email(user_email)
    else:
        user_data["Email"] = user_email

    return user_data


def check_email(user_email):
    
    com = user_email.endswith(".com") 
    at = '@' in user_email            
    
    if com == True and at == True:
        verify_email=True
    else:
        verify_email=False
        
    return verify_email



def suggest_password(user_data):
    
    first_2_letters_of_user_first_name = user_data["Name"][0:2]
    last_2_letters_of_user_last_name = user_data["Name"][-2:]
    five_random_letters = ''.join(random.choice(string.ascii_letters)for i in range(5))

    suggested_password= first_2_letters_of_user_first_name+last_2_letters_of_user_last_name+five_random_letters

    return(suggested_password)


while start == True:
    
    
    print ("\n\nWelcome to HNG tech, My name is Kelvin.")
    
    get_detail() 


    suggested_password = suggest_password(user_data)
    
    
    print ("\nMy suggested Password for you is: "+suggested_password)
    
    
    satisfaction=0 
    
    while satisfaction == 0:
        response=input("Are you satisfied with it? If  yes, Type 'Y' and 'N' for no: ")
        if response=='Y' or response=='y':
            satisfaction=1  
            
        elif response=='N' or response=='n':
            satisfaction=2  

        else:
            print ("WRONG INPUT! Please Enter 'Y' for yes or 'N' for no\n")

    else:
        if satisfaction==1:
            user_data["Password"] = suggested_password
            print("\nUser details: "+str(user_data))

        else :
            print("\nOkay, Note that your password should be at least 7 characters")
            user_password=input("\nPlease enter your preferred password: ")
        
            while len(user_password)<7:
                print("PASSWORD TOO SMALL! \n Note that password should be at least 7 characters long")
                user_password=input("\nPlease enter your  preferred password: ")
            else:
                user_data["Password: "] = user_password
                print("\nUser details: "+str(user_data))

    user_id+=1
    container[user_id] = user_data
    user_data={}
    
    print ("Details successfully saved.")
    status = input("\nEnter 'Y' for a fresh record or any other key to Exit: ")
    if status == 'Y' or status == 'y':
        start = True
    else:
        start = False

print ("Here are the details of registered user.\n")
user_id+=1
for i in range (1,user_id):
    print (container[i])