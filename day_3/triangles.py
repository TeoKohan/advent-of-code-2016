with open('input') as input:
      text = input.read()
      triangles = text.split('\n')[:-1]
      triangles = [ triangle.split('  ')[1:] for triangle in triangles ]
      triangles = [ [int(side.strip()) for side in triangle if side.strip() != ''] for triangle in triangles ]

      column_triangles = list(zip(*triangles))
      column_triangles = [[list(line[i:i+3]) for i in range(0, len(line), 3)] for line in column_triangles]
      column_triangles = [item for line in column_triangles for item in line]
      
      def possible_triangles(triangles): 
            possible = 0
            for a, b, c in triangles:
                  if (a + b > c) and (a + c > b) and (b + c > a):
                        possible += 1
            return possible

with open('output', 'w') as output:
      output.write( str(possible_triangles(triangles)) + '\n' )
      output.write( str(possible_triangles(column_triangles)) + '\n' )