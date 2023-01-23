'''
Python script to calculate the newton interpolation
'''

def calculate_newton_interpolation(find_x:float, x:list, fx:list) -> float:
    '''
    Calculate newton interpolation

    :param find_x: Value to look for
    :type find_x: int
    :param x: Values of x
    :type x: list
    :param fx: Values of fx
    :type fx: list
    :returns: Approximation of the value that x would have
    :rtype: float
    '''
    
    matrix = [fx, *[[0 for _ in range(len(fx) - 1)] for _ in range(len(fx) - 1)]]
    numbers_amount = len(x)

    for i in range(numbers_amount):
        nums_list = matrix[i]
        for j in range(numbers_amount):
            if j+1 == numbers_amount == i+1 or j+i+1 >= numbers_amount: continue
            value = (nums_list[j+1] - nums_list[j]) / (x[j+i+1] - x[j])
            matrix[i+1][j] = value
    
    find_x = 4
    values_x_mult = []
    for i, value in enumerate(x):
        if i == 0:
            res = (find_x - value)
            values_x_mult.append(res)
            continue
        mult = (find_x - value) * (values_x_mult[i-1])
        values_x_mult.append(mult)
    
    first_number = [_list[0] for _list in matrix]
    res_sum = []
    for i, value_i in enumerate(first_number[1:]):
        res_sum.append(value_i * values_x_mult[i])
    res_sum.insert(0, first_number[0])

    return sum(res_sum)
