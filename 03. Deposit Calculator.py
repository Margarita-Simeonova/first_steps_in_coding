def deposit_calculator(deposit_sum, period_in_mounts, interest_rate):
    # calculate money
    
    total_sum = deposit_sum + period_in_mounts * ((deposit_sum * interest_rate / 100) / 12)

    return total_sum


# input from console
deposit = float(input())
mounts = int(input())
percent = float(input())
result = deposit_calculator(deposit, mounts, percent)

print(result)
