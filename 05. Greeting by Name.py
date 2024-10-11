def greeting_by_name(name):
    greeting = f"Hello, {name}!"
    return greeting


name_arg = input()
result = greeting_by_name(name_arg)
print(result)
