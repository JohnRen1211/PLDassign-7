# Program for password validator
# Making command program
print("Welcome to the system can you input a paswword? Type ""Y"" for yes and ""N"" for no command.")

response = input("response: ")
if response == ("Y"):
   print("Continue to the survey")
elif response == ("N"):
   print("Okay, then rest.")
   raise SystemExit
elif response != "Y" or "N":
     print("Put Valid Value")

#Making fucntion for password

def password_valid(password):
    Special_character = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">"]
    val = True 

    if len(password) < 15:
        print ("Length of password must not be less than 15")
        val = False
    
    if len (password) > 15:
       print("Length of password must not be greater than 15")
       val = False
    
    if not any (char.isdigit() for char in password):
        print("Password must have numerical character")
        val = False
    
    if not any (char.isupper() for char in password):
        print("Password must have upper case character")
        val = False

    if not any (char.islower() for char in password):
        print("password must have lower case")
        val = False
    
    if not any (char in Special_character for char  in password):
        print("Password must have special character")
        val = False

    if val:
        return val
        
#The main method to calling the fucntion
def main():
    password = input("Enter sample password: ")
    if (password_valid(password)):
        print ("Password valid")
    else:
        print("Input valid password")

