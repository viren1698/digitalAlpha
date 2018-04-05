n = int(input("Enter the number of elements in the fibonacci series : "))
first = 0
second = 1
fibonacci_list = [first, second]
for i in range(n):
  third = first + second
  first = second
  second = third
  fibonacci_list.append(third)
print(fibonacci_list)
