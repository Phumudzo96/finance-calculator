import math

# Explain everything the user needs to know about interest and investment
print("Choose either 'INVESTMENT' or 'BOND' from the meun below to proceed: ")
print("Investment   -   to calculate the amount of interest you'll earn on interest")
print("Bond   -   to calculate the amount you'll have to pay on a home loan")

# Ask the user which investment they would love to use
investment_calculator = input("Choose type of investment between 'investment' and 'bond' ")

# Start calculating based on the type of investment that was choosen
if (investment_calculator == "investment") or (investment_calculator == "Investment") or (investment_calculator == "INVESTMENT"):
    amount = float(input("How much money are you going to deposit: "))
    interest_rate = int(input("How much is the interest rate: "))
    years = int(input("Number of years you are investing: "))
    interest = input("Is it a 'Compound' or 'Simple' interest: ")
    if interest == "compound" or interest == "Compound" or interest == "COMPOUND":      # if the user selected INVESTMENT, calculate between "compound" and "simple"
        intrest_rate1 = interest_rate / 100
        cost = amount * math.pow((1 + intrest_rate1), years)
        final_cost = round(cost, 2)
        print(f"The final cost for the compound interest is R{final_cost}")
    elif interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        interest_rate2 = interest_rate / 12
        cost = amount * (1 + interest_rate2 * years)
        final_cost = round(cost, 2)
        print(f"The final cost for the simple interest is R{final_cost}")
    else:
        print("Invalis selection")

if (investment_calculator == "bond") or (investment_calculator == "Bond") or (investment_calculator == "BOND"):
    house = float(input("What is the current value of the house: "))
    interest_rate = int(input("What is the interest rate: "))
    months = int(input("How many months are left to pay off the the house: "))
    interest_rate1 = interest_rate / 12
    cost = interest_rate1  * house / (1 - (1 + interest_rate1) **( - months))
    final_cost = round(cost, 2)
    print(f"The monthly payments of the bond is R{final_cost}")