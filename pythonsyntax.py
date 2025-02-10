
print("Welcome to Python Pizza Deliveries!")

# Get user inputs
size = input("What size pizza do you want? (S, M, L): ").upper()
add_pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

# Set base prices
prices = {"S": 15, "M": 20, "L": 25}
pepperoni_prices = {"S": 2, "M": 3, "L": 3}
cheese_price = 1

# Calculate total bill
bill = prices.get(size, 0)

if add_pepperoni == "Y":
    bill += pepperoni_prices.get(size, 0)

if extra_cheese == "Y":
    bill += cheese_price

print(f"Your final bill is: ${bill}.")