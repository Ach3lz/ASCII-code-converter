name = input("kindly input your name: ")




income= {}
def add_income():
    sources = int(input("how many sources of income do you have"))
    for i in range(1,sources+1):
        income_source = input("kindly input your income source: ")
        income_amount = int(input("kindly input your income amount: "))
        income[income_source] = income_amount
    home()

expenses = {}
def add_expenses():
    sources = int(input("how many sources of expenses do you have"))
    for i in range(1,sources+1):
        expenses_source = input("kindly input your expenses source: ")
        expenses_amount = int(input("kindly input your expenses amount: "))
        expenses[expenses_source] = expenses_amount
    home()
        
def saving_goal():
    saving_goal = input("what is your saving goal for the month? : ")
    print(f"your saving goal is {saving_goal} cedis")
    home()
    
def home():
    print(f"welcome {name}")
    print("1. add income")
    print("2. add expenses")
    print("3. add saving goal")
    print("4. view income statement")
    print("5. view expenses statement")
    next_step = int(input("what would you like to do today? : "))
    
    if next_step == 1:
        add_income()
    elif next_step==2:
        add_expenses()
    elif next_step==3:
        saving_goal()
        home()
    elif next_step==4:
        print(f"hi {name} your income statement should be seen below")
        print(income)
        home()
    elif next_step==5:
        print(f"hi {name} your expense statement should be seen below")
        print(expenses)
    
home()

    

    
        

    