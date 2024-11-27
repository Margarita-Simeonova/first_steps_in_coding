def yard_greening(yard_area_in_square_meters):
    
    price_without_discount = yard_area_in_square_meters * 7.61
    discount = price_without_discount * 0.18
    total_price = price_without_discount - discount
    result = f"The final price is: {total_price:.2f} lv.\nThe discount is: {discount:.2f} lv."

    # return result
    return result


# take input
yard_area_in_square_meters_arg = float(input())
result = yard_greening(yard_area_in_square_meters_arg)

# print result
print(result)
