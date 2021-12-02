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


