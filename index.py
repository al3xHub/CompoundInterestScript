import time
# Compound interest calculator
initial_principal = 0
rate = 0
time = 0

while True :
    try:
        initial_principal = float(input("Enter the initial principal amount:"))
        if initial_principal < 0:
            print("Invalid amount. Can't be less or equal than zero.")
        else:
            break
        
    except:
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        
while True :
    try:
        rate = float(input("Enter the interest rate:"))
        if rate < 0 :
            print("Invalid interest amount. Can't be less or equal than zero.")
        else:
            break
    except:
        print("Invalid input. Please enter a number.")

while True :
    try:
        time = int(input("Enter the time in years:"))
        if time < 0 :
            print("Time can't be less or equal than zero.")
        else:
            break
    except:
        print("Invalid input. Please enter a number.")
        
total = initial_principal * pow((1 + rate / 100), time)

print(f"The total amount after {time} years is: €{total:.2f}")


