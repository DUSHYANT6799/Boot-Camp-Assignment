def calculate_simple_interest(principal, time, is_female, is_senior_citizen):
    if is_female and is_senior_citizen:
        rate = 8
    elif is_female and not is_senior_citizen:
        rate = 6
    elif not is_female and is_senior_citizen:
        rate = 7
    else:
        rate = 5

    interest = (principal * rate * time) / 100
    return interest

# Example usage
principal = 10000
time = 2
is_female = True
is_senior_citizen = True

interest = calculate_simple_interest(principal, time, is_female, is_senior_citizen)
print(f"The simple interest for the customer is: {interest}")