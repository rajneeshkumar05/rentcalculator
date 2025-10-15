rent = int(input("Enter the rent amount: "))
food = int(input("Enter the food expenses: "))
electricity = int(input("Enter the electricity expenses: "))
charge_per_unit = float(input("Enter the charge per unit of electricity: "))
persons_living_in_flat = int(input("Enter the number of persons living in the flat: "))
total_electricity_bill = electricity * charge_per_unit

total_expenses = rent + food + total_electricity_bill
individual_share = total_expenses / persons_living_in_flat
print("Each person should pay:", individual_share)

