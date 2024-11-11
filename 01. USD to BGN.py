ONE_DOLLAR_PRICE = 1.79549


def usd_to_bgn(dollars):
    bgn = dollars * ONE_DOLLAR_PRICE

    return bgn


#get input
dollars_count = float(input())
result = usd_to_bgn(dollars_count)

#print result
print(result)
