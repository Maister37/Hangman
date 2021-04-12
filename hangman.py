import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, help="increase output verbosity", required=True)
parser.add_argument('--principal', type=int, help="increase output verbosity", required=True)
parser.add_argument('--payment', type=int, help="increase output verbosity")
parser.add_argument('--periods', type=int, help="increase output verbosity")
parser.add_argument('--interest', type=float, help="increase output verbosity")
args = parser.parse_args()
if args.type == 'diff':
    if len(args) != 5:
        print("Incorrect parameters.")
    else:
        c_p = args.principal
        number_o_m = args.periods
        credit_i = args.interest / 1200
        calculate_differentiated_payment()
elif args.type == 'annuity':
    if len(args) != 5:
        print("Incorrect parameters.")
    else:
        c_p = args.principal
        number_o_m = args.periods
        credit_i = args.interest / 1200
        annuity_m_p = args.payment
        if c_p == None:
            calculate_credit_principal()
        elif number_o_m == None:
            calculate_months()
        elif annuity_m_p == None:
            calculate_annuity_payment()
else:
    print("Incorrect parameters.")


def calculate_months():
    c_p = int(input("Enter the credit principal: "))
    annuity_m_p = int(input("Enter the monthly payment: "))
    credit_i = float(input("Enter the credit interest: ")) / 100
    nominal_i_r = (credit_i / (12 * 1))
    number_o_m = math.ceil(math.log((annuity_m_p / (annuity_m_p - nominal_i_r * c_p)), (1 + nominal_i_r)))
    if number_o_m == 1:
        print("You need 1 month to repay this credit!")
    elif 12 > number_o_m > 1:
        print(f"You need {number_of_months} months to repay this credit!")
    else:
        years = number_o_m // 12
        leftover_months = number_o_m % 12
        if leftover_months != 0:
            if years > 1:
                if leftover_months > 1:
                    print(f"You need {years} years and {leftover_months} months to repay this credit!")
                else:
                    print(f"You need {years} years and {leftover_months} month to repay this credit!")
            else:
                print(f"You need {years} year to repay this credit!")
        else:
            print(f"You need {years} years to repay this credit!")


def calculate_annuity_payment():
    c_p = int(input("Enter the credit principal: "))
    number_of_months = int(input("Enter the number of periods: "))
    credit_interest = (float(input("Enter the credit interest: "))) / 1200
    annuity_m_p = c_p * ((credit_i * ((1 + credit_i) ** number_o_m)) / (((1 + credit_i) ** number_o_m) - 1))
    print(f"Your annuity payment = {math.ceil(annuity_m_p)}!")


def calculate_credit_principal():
    annuity_m_p = float(input("Enter the monthly payment: "))
    number_o_m = int(input("Enter the number of periods: "))
    credit_i = float(input("Enter the credit interest: ")) / 1200
    c_p = annuity_m_p / (((credit_i * (1 + credit_i) ** number_o_m)) / ((1 + credit_i) ** number_o_m - 1))
    print(f"Your credit principal = {c_p}!")
    
def calculate_differentiated_payment():
    c_p = int(input("Enter the credit principal: "))
    number_o_m = int(input("Enter the number of periods: "))
    credit_i = (float(input("Enter the credit interest: "))) / 1200
    i = 0
    overall = 0
    while i < number_o_m:
        i += 1
        differentiated_payment = math.ceil(float((c_p / number_o_m) + credit_i * (c_p - (c_p * (i - 1)) / number_o_m)))
        overall += differentiated_payment
        print(f"Month {i}: paid out {differentiated_payment}")
    print(f"Overpayment = {overall - c_p}")






choice = input("""What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal: """)



if choice == "n":
    calculate_months()
elif choice == "a":
    calculate_annuity_payment()
elif choice == "p":
    calculate_credit_principal()
