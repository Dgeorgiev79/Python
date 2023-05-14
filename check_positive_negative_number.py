number = float(input())

message = ' '

if number == 0:
    message = 'zero'

elif number > 0:
    if number < 1:
        message = 'small positive'
    elif number > 1000000:
        message = 'large positive'
    else:
        message = 'positive'
else:
    if abs(number) < 1:
        message = 'small negative'
    elif abs(number) > 1000000:
        message = 'large negative'
    else:
        message = 'negative'

print(f'{message}')
