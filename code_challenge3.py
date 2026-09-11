#Global Freight Calculator
express = "t"
international = "t"

name = input("Sender Name: ")
type = input("Type of Item: ")
is_Fragile = input("Is is Fragile? (t/f): ")
weight = float(input("Enter weight{kg}: "))
distance = float(input("Enter distance{km}: "))
is_express = input("Is it Express? (t/f): ")
is_international = input("Is it International? (t/f): ")

#Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

#Evaluate Pricing Tiers
if weight <= 2.0 and distance <= 100 and express != is_express and international != is_international:
	print("total: ₱0.00")

elif is_express == express and is_international == international :
	print("total amount: ₱",base_cost * 1.40 + 50,)

elif is_express == express or is_international and weight > 20 :
	print("total amount: ₱", base_cost * 1.20 + 25,)

elif weight > 30 or distance > 1000:
	print("total amount: ₱", base_cost + 30,)

else:
	print("main total: ₱", base_cost,)

