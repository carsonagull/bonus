def calculate_bonus(salary, years_of_service):
    if years_of_service > 10:
        bonus_percentage = 10
    elif 6 <= years_of_service <= 10:
        bonus_percentage = 8
    else:
        bonus_percentage = 5
    bonus_amount = (bonus_percentage / 100) * salary
    return bonus_amount

print("BOSS Karibu to the Bonus Calculator! ")

salary = float(input("Please enter your current salary in Kenyan Shillings (KES): "))
years_of_service = int(input("And how many years have you been with the company? "))

bonus = calculate_bonus(salary, years_of_service)

print(f"MKUU HABARI NDIO HII! Based on your {years_of_service} years of service, you've earned a bonus of KES {bonus:.2f}. BIG UP YOOOH")