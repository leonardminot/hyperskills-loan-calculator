import math


def get_months_to_repay(loan_principal: int, monthly_payment: int) -> int:
    return math.ceil(loan_principal / monthly_payment)


def get_monthly_loan(loan_principal, number_of_repay_month):
    return math.ceil(loan_principal / number_of_repay_month)


def get_last_loan(loan_principal, number_of_repay_month):
    return loan_principal - (number_of_repay_month - 1) * get_monthly_loan(loan_principal, number_of_repay_month)


def print_number_of_month_to_repay(number_of_repay_month):
    return f"It will take {number_of_repay_month} {'month' if number_of_repay_month == 1 else 'months'} " \
           f"to repay the loan"


def print_monthly_loan(monthly_loan, last_payment=0):
    return f"Your monthly payment = {monthly_loan}" \
           f"{'' if last_payment == 0 else f' and the last payment = {last_payment}.'}"


if __name__ == '__main__':
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("What do you want to calculate?")
    print('type "m for number of monthly payments,')
    print('type "p" for the monthly payment:')
    user_choice = input()

    if user_choice == "m":
        print("Enter the monthly payment:")
        monthly_payment = int(input())
        month_to_repay = get_months_to_repay(loan_principal, monthly_payment)
        print(print_number_of_month_to_repay(month_to_repay))
    else:
        print("Enter the number of months:")
        number_of_month = int(input())
        monthly_loan = get_monthly_loan(loan_principal, number_of_month)
        last_loan = get_last_loan(loan_principal, number_of_month)
        print(print_monthly_loan(monthly_loan, last_loan))
