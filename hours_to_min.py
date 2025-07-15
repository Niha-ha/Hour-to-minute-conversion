def hr_min(hour):
    return hour*60

hr = float(input("Enter hour to convert:"))
minutes = hr_min(hr)
print(f"{hr} hours is {minutes} minutes")