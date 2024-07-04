bold_text = "\033[1m"

reset_text = "\033[0m"

text_color = "\033[34m"

underline = "\033[4m"

These are universal variables that manipulate the strings in the code when printed out

def intro():
    
    print("============================================= ")
    print(bold_text+text_color+"Welcome to Aithusa ASCII converter"+reset_text)
    print("============================================= ")
intro()

This is a function which contains the introduction of our program which welcomes the user to "Aithusa ASCII converter.



def ASCII_converter():
    user_character = input(underline+text_color+"Kindly enter your character to be converted: "+reset_text)
    for i in user_character:
        print(ord(i),end=".")
    print()
ASCII_converter()

This is another function that requests for the character from the user and uses the ord() function to convert it to its ASCII code.

for i in user_character:
        print(ord(i),end=".")


  This code uses a for loop to convert each string to its corresponding values and separates them using the 'endl=' code to print out the results horizontally 


  
  
    while True:
    print(ASCII_converter())

This code uses a while loop to keep running the code in the ASCII_converter() function

