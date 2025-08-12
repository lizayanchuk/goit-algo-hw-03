# Завдання 2
import random

def get_numbers_ticket(min, max, quantity):
  if min >= max:
      return []
  if quantity > (max - min+1):
      return []
  if min < 1 or max < 1 or min > 1000 or max > 1000:
      return []

  nums = random.sample(range(min, max+1), quantity)
  return sorted(nums)

while True:
  try:
    min = int(input("Введіть мінімальне число: "))
    max = int(input("Введіть максимальне число: "))
    quantity = int(input("Введіть кількість: "))

    lottery = get_numbers_ticket(min, max, quantity)

    if not lottery:
      print("Параметри введено не правильно. Спробуйте ще раз!")
      continue

    print("Ваші числа: ", lottery)
    break

  except Exception as e:
    print(f"Виникла помилка: {e}. Спробуйте ще раз!")

# без циклу
get_numbers_ticket(10,14,6)
