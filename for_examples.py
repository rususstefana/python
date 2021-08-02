letters = 'agsicccgdbcbv'

for c in letters:
    print(c)

for i in range(5):
    print(i)

for i in range(len(letters)):
    print(i, letters[i])

for i, c in enumerate(letters):
    print(i, c)