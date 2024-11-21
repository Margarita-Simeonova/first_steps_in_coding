def concatenate_data(first_name: str, last_name: str, age: int, town: str):
    
    greeting = f"You are {first_name} {last_name}, a {age}-years old person from {town}."
    
    # return result
    return greeting


first_name_arg = input()
last_name_arg = input()
age_arg = int(input())
town_arg = input()
result = concatenate_data(first_name_arg, last_name_arg, age_arg, town_arg)

# print result
print(result)
