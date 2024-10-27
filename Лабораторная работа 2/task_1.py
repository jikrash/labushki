money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
months = 0

current = money_capital + salary

while current >= spend:
  if months > 0:
    spend *= (1 + increase)
  current -= spend
  current += salary
  months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)