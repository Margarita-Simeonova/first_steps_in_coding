def basketball_equipment(subscription):
    
    sneakers_price = subscription * 0.6
    equipment_price = sneakers_price - (sneakers_price * 0.2)
    ball_price = equipment_price / 4
    accessories_price = ball_price / 5

    total_expenses = subscription + sneakers_price + equipment_price + ball_price + accessories_price

    # return result
    return total_expenses


# input from console
tax = float(input())
result = basketball_equipment(tax)

# print result
print(result)
