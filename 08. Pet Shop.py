def pet_shop(dogs_food_count, cats_food_count):
    CATS_FOOD_PRICE = 4
    DOGS_FOOD_PRICE = 2.5
    total_price = (cats_food_count * CATS_FOOD_PRICE) + (dogs_food_count * DOGS_FOOD_PRICE)
    return total_price


dogs_food_count_arg = int(input())
cats_food_count_arg = int(input())
result = pet_shop(dogs_food_count_arg, cats_food_count_arg)
print(result)
