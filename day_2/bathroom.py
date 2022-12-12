class Vector2:
      def __init__(self, x, y):
            self.x = x
            self.y = y

      def __add__(self, v):
            return Vector2(self.x + v.x, self.y + v.y)

      def __iter__(self):
            yield self.x
            yield self.y

D = {
      'U': Vector2( 0, -1),
      'R': Vector2( 1,  0),
      'D': Vector2( 0,  1),
      'L': Vector2(-1,  0)
}

square = {
      (-1, -1): '1',
      ( 0, -1): '2',
      ( 1, -1): '3',
      (-1,  0): '4',
      ( 0,  0): '5',
      ( 1,  0): '6',
      (-1,  1): '7',
      ( 0,  1): '8',
      ( 1,  1): '9'
}

diamond = {
      ( 0, -2): '1',
      (-1, -1): '2',
      ( 0, -1): '3',
      ( 1, -1): '4',
      (-2,  0): '5',
      (-1,  0): '6',
      ( 0,  0): '7',
      ( 1,  0): '8',
      ( 2,  0): '9',
      (-1,  1): 'A',
      ( 0,  1): 'B',
      ( 1,  1): 'C',
      ( 0,  2): 'D'
}

solution = ''
diamond_solution = ''
with open('input') as input:
      text = input.read()
      code = text.split('\n')[:-1]

      finger = Vector2( 0,  0)
      for line in code:
            for char in line:
                  finger = finger + D[char] if abs((finger + D[char]).x) <= 1 and abs((finger + D[char]).y) <= 1 else finger
            solution += square[tuple(finger)]

      finger = Vector2(-2,  0)
      for line in code:
            for char in line:
                  finger = finger + D[char] if abs((finger + D[char]).x) + abs((finger + D[char]).y) <= 2 else finger
            diamond_solution += diamond[tuple(finger)]

with open('output', 'w') as output:
      output.write( solution + '\n')
      output.write( diamond_solution + '\n')
