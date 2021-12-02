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

# Coding program for the counting word
sentence = input("Type a sample sentence : ")
word= 1
vowels = 0
consonants = 0
sentence.upper() 

for i in range(len(sentence)):
    if(sentence[i] == ' ' or sentence == '\n' or sentence == '\t'):
       word = word + 1  
print("the total numbers of words=", word) 
