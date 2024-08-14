from datetime import datetime

today = datetime.now() 
dateofbirth= datetime(1990, 8, 27)
if today.month>dateofbirth.month or (today.month==dateofbirth.month and (today.day >= dateofbirth.day)):
        age = today.year-dateofbirth.year 


else:
    age= today.year- dateofbirth.year-1

print(age)
