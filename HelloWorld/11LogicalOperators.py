has_high_income = False
has_good_credit = True
has_criminal_records = False

# Both conditions should be true
if has_high_income and has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible for Loan")

# Any one Can be true
if has_high_income or has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible for Loan")

# Reverses the boolean value
if not has_criminal_records and has_good_credit:
    print("Eligible for Loan")
else:
    print("Not eligible for Loan")