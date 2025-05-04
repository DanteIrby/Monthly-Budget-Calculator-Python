def calculate_monthly_budget():
    """Calculates total monthly bills, total monthly income, and the leftover income."""

    # --- Define Variables for Bills ---
    print("--- Enter Your Monthly Bills ---")
    electricity_bill = int(input('Electricity: '))
    phone_bill = int(input('Phone: '))
    car_payment = int(input('Car Payment: '))
    insurance_cost = int(input('Insurance: '))
    rent_payment = int(input('Rent: '))
    subscriptions_cost = int(input('Subscriptions: '))
    credit_card_payment = int(input('Credit Card Payment: '))
    extra_debt_payment = int(input('Extra Debt Owed: '))
    extra_bills_cost = int(input('Other Bills: '))

    total_bills = (electricity_bill + phone_bill + car_payment + insurance_cost +
                   rent_payment + subscriptions_cost + credit_card_payment +
                   extra_debt_payment + extra_bills_cost)

    print(f'\nTotal Monthly Bills: ${total_bills:.2f}')

    # --- Define Variables for Income ---
    print("\n--- Enter Your Monthly Income ---")
    primary_income = int(input('Primary Income: '))
    secondary_income = int(input('Secondary Income: '))
    extra_income = int(input('Extra Income: '))

    total_income = primary_income + secondary_income + extra_income
    print(f'Total Monthly Income: ${total_income:.2f}')

    # --- Calculate Leftover Income and Provide Feedback ---
    leftover_income = total_income - total_bills

    print("\n--- Budget Summary ---")
    if total_income > total_bills:
        print(f'You have enough to pay your bills this month! '
              f'You will have ${leftover_income:.2f} left over.')
    else:
        print(f'You do not have enough money this month. '
              f'You need ${abs(leftover_income):.2f} more to cover all your bills.')

if __name__ == "__main__":
    calculate_monthly_budget()