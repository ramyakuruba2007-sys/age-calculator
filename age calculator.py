from datetime import date
print("****Age Calculator****")
birth_year=int(input("Enter birth year(YYYY): "))
birth_month=int(input("Enter birth month(1-12): "))
birth_day=int(input("Enter birth day(1-31): "))
today=date.today()
birth_date=date(birth_year,birth_month,birth_day)
age=today.year-birth_date.year
# Check if birthday has occurred this year
if(today.month,today.day)<(birth_date.month,birth_date.day):
    age-=1
    print("\nYour Age is: ",age,"years old")
