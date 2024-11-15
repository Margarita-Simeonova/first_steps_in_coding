# first option
def numbers_line():
    # numbers from 1 to 10
    
    for n in range(1, 11):
        # print number
        
        print(n)


# call func
numbers_line()

#############
# second opption
def nums_line(start_num):
    # numbers from numb_x to numb_x + 10
    
    for n in range(start_num, start_num + 10):
        # print number
        
        print(n)


# return line of numbers
number = 1
# call func
nums_line(number)
