number = int(input('Скільки піц замовляєте? '))
cost = float(input('Скільки коштує одна піца? '))

# Повна вартість без знижки
total = number * cost
print('Ціна без знижки:', total)

# Рахуємо кількість піц зі знижкою (парні номери)
discounted_pizzas = number // 2  # кожна друга піца має знижку
discount = discounted_pizzas * cost * 0.1  # 10% знижка тільки на ці піци

print('Знижка:', discount)

# Загальна сума після знижки
total_after_discount = total - discount
print('Ціна зі знижкою:', total_after_discount)

