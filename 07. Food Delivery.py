CHICKEN_MENU = 10.35
FISH_MENU = 12.4
VEGETARIAN_MENU = 8.15
DELIVERY = 2.5


def food_delivery(chicken_menu_count, fish_menu_count, vegetarian_menu_count):
    food_price = chicken_menu_count * CHICKEN_MENU + fish_menu_count * FISH_MENU\
                 + vegetarian_menu_count * VEGETARIAN_MENU
    dessert_price = food_price * 0.2
    total_price = food_price + dessert_price + DELIVERY

    return total_price


chicken_count = int(input())
fish_count = int(input())
vegetarian_count = int(input())
print(food_delivery(chicken_count, fish_count, vegetarian_count))
