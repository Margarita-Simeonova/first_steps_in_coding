ONE_DOLLAR_PRICE = 1.79549


def usd_to_bgn(dollars):
    bgn = dollars * ONE_DOLLAR_PRICE

    return bgn


dollars_count = float(input())
result = usd_to_bgn(dollars_count)

print(result)
