import sys

value = int(sys.argv[1])
initial_value = value
result = []

while value > 0:
    number_of_spaces = value - 1
    number_of_octohorpe = initial_value - number_of_spaces
    while number_of_spaces > 0:
        result.append(' ')
        number_of_spaces -=1
    while number_of_octohorpe >= 1:
        result.append('#')
        number_of_octohorpe -= 1
    print(''.join(result))
    result.clear()
    value -= 1
    number_of_octohorpe += 1
