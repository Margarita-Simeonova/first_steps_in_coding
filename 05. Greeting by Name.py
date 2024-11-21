def greeting_by_name(name):
    # define the function
    
    greeting = f"Hello, {name}!"
    
    # return the resulr
    return greeting


# get the input from console
name_arg = input()
result = greeting_by_name(name_arg)

# print result
print(result)
