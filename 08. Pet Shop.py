# defime the global variables
CATS_FOOD_PRICE = 4
DOGS_FOOD_PRICE = 2.5


def pet_shop(dogs_food_count, cats_food_count):

    total_price = (cats_food_count * CATS_FOOD_PRICE) + (dogs_food_count * DOGS_FOOD_PRICE)
    return f"{total_price} lv."


# read input
dogs_food_count_arg = int(input())
cats_food_count_arg = int(input())

# take result
result = pet_shop(dogs_food_count_arg, cats_food_count_arg)

# print result
print(result)
