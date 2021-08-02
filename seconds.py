initial_seconds = int(input('initial_seconds:'))
hours = initial_seconds // 3600
minutes = (initial_seconds % 3600) // 60
seconds = (initial_seconds % 3600) % 60

print('coneveting initila seconds:' + str(initial_seconds))
print(str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's')