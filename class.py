bold_text = "\033[1m"
reset_text = "\033[0m"
text_color = "\033[34m"
underline = "\033[4m"
def intro():
    print("============================================= ")
    print(bold_text+text_color+"Welcome to Aithusa ASCII converter"+reset_text)
    print("============================================= ")
intro()
def ASCII_converter():
    user_character = input(underline+text_color+"Kindly enter your character to be converted: "+reset_text)
    for i in user_character:
        print(ord(i),end=".")
    print()
ASCII_converter()

while True:
    print(ASCII_converter())



