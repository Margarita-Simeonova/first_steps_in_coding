def convertor(inches_value):
    # convert
    
    centimeters = inches_value * 2.54
    return centimeters


inches_value_arg = float(input())
result = convertor(inches_value_arg)

# print result
print(result)
