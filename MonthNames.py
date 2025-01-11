month_names=["January","February","March","April","May","June",
   "July","August","September","October","November","December"]

month=int(input("Enter the month (1-12): "))
if 1<=month<=12:
    monthname=month_names[month-1]
    print(f"Month {month} is {monthname}")
else:
    print("Invalid month number.")
