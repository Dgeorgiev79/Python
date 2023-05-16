count_number = int(input())

for i in range(count_number):
 number = int(input())
 if not number % 2 == 0:
  print(f"{number} is odd!")
  break
else:
  print(f"All numbers are even.")
