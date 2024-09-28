squares = [x ** 2 for x in range(10)]

print("Squares",squares)

twos = [2 ** i for i in range(8)]

print("Twos", twos)

odds = [x for x in squares if x % 2 != 0 ]

print("Odds", odds)