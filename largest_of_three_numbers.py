first_number = int(input())
second_number = int(input())
third_number = int(input())

#print(max(first_number, second_number, third_number))

output = ''
if first_number > second_number and first_number > third_number:
    output = first_number
elif second_number > first_number and second_number > third_number:
    output = second_number
else:
    output = third_number

print(f'{output}')
