# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

# you will make adeposit in a bank at 5% rate an will calculate the investement return after 3 years.

# rates per year of investment
def rate(money):
    eq=money*0.05
    return eq

def year_1(money):
    inv_return=rate(money)+money
    return inv_return

def year_2(money):
    inv_return_2=rate(year_1(money))+year_1(money)
    return inv_return_2

def year_3(money):
    inv_return_3=rate(year_2(money))+year_2(money)
    return inv_return_3


money=10000   #10.000 euros of investment
money_return=year_3(money)
print(f"Investment return is {money_return} ")


