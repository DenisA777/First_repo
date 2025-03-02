from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date
        return delta.days
    
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
        return 0

result = get_days_from_today('2021-10-09')
print(result)




import random


def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and quantity <= max - min and max >= min :
        numbers = random.sample(range(min, max+1), quantity)
        numbers.sort()
        return sorted(numbers)
    else: 
        return []

lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)



import re


def normalize_phone(phone_number):
    formatted_phone_number = re.sub(r'[^\d+]', '', phone_number).strip()
    if formatted_phone_number.startswith('+'):
        return formatted_phone_number
    if formatted_phone_number.startswith('380'):
        return '+' + formatted_phone_number

    return '+38' + formatted_phone_number
raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



