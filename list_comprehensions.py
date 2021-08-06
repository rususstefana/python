items = [1, 2, 3, 7, 9]
print(items)

#Sa se obtina o lista cu patratele nr din lista

squares = []
for item in items:
    value = item * item
    squares.append(value)

squares1 = [v*v for v in items]

print(squares)
print(squares1)
#Sa se obtina o lista cu numerele impare din items

odds = []
for nr in items:
    if nr % 2 != 0:
        odds.append(nr)

odds1 = [nr for nr in items if nr % 2 != 0]

print(odds)
print(odds1)