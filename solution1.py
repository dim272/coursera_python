import sys

digit_string = sys.argv[1]
value = 0

for x in digit_string:
    value += int(x)

print(value)