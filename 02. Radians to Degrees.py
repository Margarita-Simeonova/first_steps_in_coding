import math


def radians_to_degrees(rad):
  # calculate radians to degrees
  
    degrees = rad * 180 / math.pi

    return degrees


# get input
radians = float(input())
result = radians_to_degrees(radians)

# print result
print(result)
