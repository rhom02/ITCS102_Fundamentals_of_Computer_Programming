age = int(input("Enter your age-> "))
rev = float(input("Enter mothly revenue-> "))
cc = int(input("Enter credit score-> "))
yrs_b = int(input("Years business-> "))
has_defaults = bool(input("default history-> "))
collateral = input("collateral name-> ")
c_value = float(input("collateral value-> "))

max_limit = 0
base_fee = 0.0

#baseline
if age >= 21 and yrs_b >=2 and has_defaults == False:
    print("baseline requirements pass")

    if cc >= 720: #tier1
        max_loan = rev * 3
        print("max loan for high credit score is ", max_loan)
        print("high credit score of 720")

        #monthly revenue conditions
        if rev >= 50000:
            base_fee = max_loan * 0.015
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_loan * 0.025
            print("base fee rate is ", base_fee)

        #collateral
        if c_value >= max_loan:
            print("collateral ", collateral, "--accepted")
        else:
            print("collateral not accepted")

        #surcharge
        surcharge = max_loan * base_fee
        if c_value % 5000 != 0:
            surcharge += 250


    elif cc <= 620 and cc < 720: #tier2
        max_loan = rev * 1.5
        print("max loan is set to ", max_loan)
        if yrs_b >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("baseline fee rate is", base_fee)

        if c_value >= max_loan:
            print("collateral ", collateral, "--accepted")
        else:
            print("collateral not accepted")

    elif cc < 620: #tier3
        print("credit score too low for a loan")
    else:
        print("not tier 1")
else:
    print("rejected: high application or ineligible owner")
        

