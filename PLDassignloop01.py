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

# Coding program for vowels and consonant

for i in sentence:
   if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
        or ord(i) == 79 or ord(i) == 85
        or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
        or ord(i) == 111 or ord(i) == 117):
         vowels = vowels + 1
   elif((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
          consonants = consonants + 1

# Printing the output of the program