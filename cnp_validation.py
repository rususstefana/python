from datetime import datetime
cnp = input("Insert CNP:")
g = int(cnp[0])

if g > 0 and g <= 8:
    date = cnp[1:7]
    date_to_compare = datetime.strptime(date, '%y/%m/%d')
    print(date_to_compare)








# if g > 0 and g <= 8:
#     yy = int(cnp[1:2])
#     currentYear = datetime.now().year % 100
#     if  (g == 5 or g == 6):
#         if  yy > currentYear:
#             print("Your year is not valid")
#             exit() 
#     mm =  int(cnp[3:4])
#     currentMonth = datetime.now().month
#     if (mm > 0 and mm <= 12):
#         if yy == currentYear and mm > currentMonth:
#             print("Your month is not valid")
#             exit()
#     zz = int(cnp[5:6])        
#     currentDay = datetime.now().day        
    
