PENS_PACK_PRICE = 5.8
MARKERS_PACK_PRICE = 7.2
DETERGENT = 1.2


def supplies_for_school(pens_pack_count, markers_pack_count, detergent_litres, discount_percent):
    price = pens_pack_count * PENS_PACK_PRICE + markers_pack_count * MARKERS_PACK_PRICE + detergent_litres * DETERGENT
    total_price = price - (price * (discount_percent / 100))

    return total_price


pens = int(input())
markers = int(input())
detergent = int(input())
percent = float(input())
print(supplies_for_school(pens, markers, detergent, percent))
