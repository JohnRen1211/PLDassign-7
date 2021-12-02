# Program that will count words, vowels and consonant in a sentence.
# Creating command for asking to input
print("Welcome to the system can you input a simple sentence? Type ""Y"" for yes and ""N"" for no command.")

response = input("Response: ")
if response == ("Y"):
   print("Continue to the survey")
elif response == ("N"):
   print("Okay, then rest.")
   raise SystemExit
elif response != "Y" or "N":
     print("Put Valid Value")
     raise SystemExit
   
# Making program for word 



