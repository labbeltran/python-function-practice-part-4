def max_func(numbers):
    if not numbers:
        return 0
    return max(numbers)

#

def max_func(numbers):
    if not numbers:
        return 0
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    
    return max_num

#

def bizarro_string(str):
    return ''.join(reversed(str))

#example
input_string = "euphoria"
print(bizarro_string(input_string))

#

def num_within(number, start, end):
    return start <= number <= end

print(num_within(4, 1, 11))
print(num_within(14, 1, 11))
print(num_within(10, 1, 11))

#

def pascal(n):
    if n < 1: 
        print('Number of rows must be >= 1')
        return
    #initialize first row
    triangle = [[1]]
    #start a new row with 1
    for i in range (1, n):
        row = [1]
        #add values based on previous rows
        for j in range (1, i): 
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        #End the row with 1
        row.append(1)
        #add row to the triangle
        triangle.append(row)
    #print the triangle by row
    for row in triangle:
        print(row)

pascal(15)