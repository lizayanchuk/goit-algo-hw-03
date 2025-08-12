# Завдання 3
import re

def normalize_phone(phone_number):
  cleaned_num = re.sub(r'\D', '', phone_number)
  if cleaned_num.startswith('380'):
    cleaned_num = '+' + cleaned_num
  else:
    cleaned_num = '+38' + cleaned_num
  return cleaned_num

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 asf  "
]

phones = [normalize_phone(phone) for phone in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", phones)
