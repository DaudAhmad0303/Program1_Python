def cal_century_year(a):
    # Here datetime is module from which we're importing date class
    from datetime import date
    
    # here we created the date object of today's date
    todays_date = date.today()

    # print("Today's Date : ", todays_date)
    curr_year = todays_date.year
    century_age = 100 + (curr_year - a)
    return century_age
    
print('''   Welcome to the my Program   ''') 
rep = "Y"
while (rep == "Y" or rep == "y"):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    if (int(age) >= 100):
        print(f"{name}, you're above 100")
        print("Re-enter you credentials")
        continue
    messege = f"{name} your age is {age} and you'll be 100 in {cal_century_year(int(age))}"
    print(messege)
    rep = input('''Do you want to test it again? Y/N
Your choice: ''')
