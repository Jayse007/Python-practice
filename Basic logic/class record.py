class_attendance = []

while True:
    print("Enter the name of one of your classmate who is present or leave blank to stop the program.")

    attendance = input()

    if attendance == '':
        break
    
    class_attendance.append(attendance)
print(class_attendance)