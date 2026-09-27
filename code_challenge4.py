# age (integer)
# is_employed (boolean)
# credt_score (integer)
# annual_income (float)
# has_collateral (boolean)

# Login System 
print("===== Loan System Login ===== ")
username = "minii"
password = "rhom02"

u = input("Input username ---> ")
p = input("Input password ---> ")

if u == username and p == password:
    print("\nLogin successful!\n")
else:   
    print("Login failed: Invalid username or password. ")

# Loanee first name and job description 
first_name = input("Enter your first name ---> ")
job_description = input("Enter your job description ---> ")

# Inputs
age = int(input("How Old are you?---->   "))
is_employed = input("Are you employed? True or False---->   ")  == "True"
credit_score = eval(input("What is your credit score?---->   "))
annual_outcome = eval(input("What is your annual income?---->   "))
has_collateral = input("Do you have Collateral? True or False---->   ") == "True"

# Maximum Age for Loan
if age > 65:
    print("Rejected: Maximum Age for Loan is 65. ")
    
if age < 21:
    print ("Rejected: Fails baseline criteria. You must 21 or older ")
    
# Name/Description of Collateral 
collateral_value = 0
if has_collateral == True:
    collateral_description = input("Enter name/description of collateral (e.g motorcycle, land, house): ")
    collateral_value = int(input("Enter value of collateral: "))
    
else:    
    print("Invalid collateral value.")
    
# Value of Collateral 
if collateral_value < 30000:
    print ("Rejected: Collateral value is invalid. Minimum is 30000 ")
else:
    print("Collateral accepted ")
    
# Loan Calculation
base_rate = 0.0
eligible = False

#Baseline eligibilty criteria for loan approval and Tier 1
base_rate = 0.0
if age >= 21 and is_employed is True:
  print("Passed baseline eligibility ")
  if credit_score >= 750:
    print("Your credit score is above 750")
    if annual_outcome >= 100000:
      print("You have a high annual income")
      baseline_interest_rate = 4.5
      print("Hi, your interest rate is ", baseline_interest_rate, "%")
    else:
        baseline_interest_rate = 5.0
        print("You are eligible for a loan with an interest rate of", baseline_interest_rate, "%")
        
#Tier 2 eligibility criteria for loan approval
  elif credit_score >= 600 and credit_score < 750:
    if has_collateral == True:
      base_interest_rate = 7.0
      print("Hi, your interest rate is ", base_interest_rate, "%")
    elif has_collateral == False and annual_outcome < 40000:
      base_interest_rate = 9.5
      print("Hi, your interest rate is ", base_interest_rate, "%")
    else:
      base_interest_rate = 8.0
      print("You are eligible for a loan with an interest rate of", base_interest_rate,  "%")


#Tier 3 eligibility criteria for loan approval
  elif credit_score < 600:
    print("Rejected: Credit score too low ")

# Amount to Loan and Calculated Interest Rate using base rate
base_rate = 0.0

if eligible == False:
    loan_amount = int(input("Enter amount you want to loan: "))
    if loan_amount <= 0:
        print("Invalid loan amount.")
    
else:
    print("Invalid loan amount ")
    
# Interest Calculation for 1 year
interest_amount = loan_amount * (base_rate / 100)
total_payable = loan_amount + interest_amount
monthly_payment = total_payable / 12

print("\n===== LOAN SUMMARY =====")
print("Loanee: ", first_name, "-", job_description)
print("Age: ", age, "Employed: ", is_employed)
if has_collateral:
    print("Collateral: " , collateral_description)
    print("Value: " , collateral_value)
    print("Loan Amount: ", loan_amount)
    print("Interest Rate: ", base_rate, "%")
    print("Interest to Pay: ", interest_amount)
    print("Total Payable (1 year): ", total_payable)
    print("Monthly Payment: ", monthly_payment)
    print("\n===== Status: APPROVED =====")
    