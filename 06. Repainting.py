NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
THINNER_PRICE = 5
GARBAGE_BAGS = 0.4


def repainting(nylon, paint_litres, thinner_litres, hours_to_work):
    materials_price = ((nylon + 2) * NYLON_PRICE) + ((paint_litres + paint_litres * 0.1) * PAINT_PRICE)\
                      + thinner_litres * THINNER_PRICE + GARBAGE_BAGS
    workers_salary = (materials_price * 0.3) * hours_to_work
    total_expense = materials_price + workers_salary

    return total_expense


nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
result = repainting(nylon, paint, thinner, hours)

print(result)
