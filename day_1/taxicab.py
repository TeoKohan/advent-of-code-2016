D = {
      ( 0, -1): {'R': ( 1,  0), 'L': (-1,  0)},
      ( 1,  0): {'R': ( 0,  1), 'L': ( 0, -1)},
      ( 0,  1): {'R': (-1,  0), 'L': ( 1,  0)},
      (-1,  0): {'R': ( 0, -1), 'L': ( 0,  1)}
}

with open('input') as input:
      text = input.read()
      directions = text.split(',')
      directions = [direction.strip() for direction in directions]
      directions = [(direction[0], int(direction[1:])) for direction in directions]

      direction  = (0, -1)
      position   = (0,  0)
      visited    = {(0, 0)}
      revisited  = []
      for turn, walk in directions:
            direction = D[direction][turn]
            for step in range(walk):
                  position  = (position[0] + direction[0], position[1] + direction[1])
                  if position in visited:
                        revisited += [position]
                  else:
                        visited.add(position)

with open('output', 'w') as output:
      output.write( str(abs(position[0]) + abs(position[1])) + '\n')
      output.write( str(abs(revisited[0][0]) + abs(revisited[0][1])) + '\n')