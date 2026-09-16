age = int(input("How Old are you?---->   "))
is_employed = input("Are you employed? True or False---->   ")  == "True"
credit_score = eval(input("What is your credit score?---->   "))
annual_outcome = eval(input("What is your annual income?---->   "))
has_collateral = input("Do you have Collateral? True or False---->   ") == "True"

#Baseline eligibilty criteria for loan approval and Tier 1
base_rate = 0.0
if age >= 21 and is_employed is True:
  print("Passed baseline eligibility ")
  if credit_score >= 750:
    print("Your credit score is above 750")
    baseline_interest_rate = 5.0
    print("Hi, your interest rate is ", baseline_interest_rate, "%")
    if annual_outcome >= 100000:
      print("You have a high annual income")
      baseline_interest_rate = 4.5
      print("Hi, your interest rate is ", baseline_interest_rate, "%")
    else:
        print("You are eligible for a loan with an interest rate of", baseline_interest_rate, "%")

#Tier 2 eligibility criteria for loan approval
  elif credit_score >= 600 and credit_score < 750:
    base_interest_rate = 8.0
    if has_collateral == True:
      print("Hi, your interest rate is ", baseline_interest_rate, "%")
      base_interest_rate = 7.0
      print("Hi, your interest rate is ", baseline_interest_rate, "%")
    elif has_collateral == False and annual_outcome < 40000:
      base_interest_rate = 9.5
      print("Hi, your interest rate is ", baseline_interest_rate, "%")
    else:
      print("You are eligible for a loan with an interest rate of", base_interest_rate,  "%")


#Tier 3 eligibility criteria for loan approval
  elif credit_score < 600:
    print("You are not eligible for a loan at this time. Please work on improving your credit score and financial situation before applying again.")


else:
  print("You are not eligible for a loan at this time.")