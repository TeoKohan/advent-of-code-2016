with open('input') as input:
      text = input.read()
      scrambled_messages = text.split('\n')[:-1]

letters     = list(map(list, scrambled_messages))
by_position = zip(*letters)
by_position = list(map(''.join, by_position))

most_common = [ max(position, key=position.count) for position in by_position ]
max_code    = ''.join(most_common)

least_common = [ min(position, key=position.count) for position in by_position ]
min_code     = ''.join(least_common)

with open('output', 'w') as output:
      output.write( max_code + '\n')
      output.write( min_code + '\n')
