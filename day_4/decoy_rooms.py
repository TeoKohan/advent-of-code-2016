import re
from collections import Counter

with open('input') as input:
      text = input.read()
      rooms = text.split('\n')[:-1]
      rooms = [room.rsplit('-', 1) for room in rooms]
      rooms = [[''.join(name.split('-')), int(data.split('[')[0]), data.split('[')[1][:-1]] for name, data in rooms]
      real_rooms = []

      def real_room(room):
            name, id, hash = room
            D = Counter(name)
            D = sorted(D.items(), key=lambda v: (-v[1], v[0]))
            for i in range(5):
                  if hash[i] != D[i][0]:
                        return False
            return True
      
      def decode_room(room):
            name, id, hash = room
            shift = id % 26
            name = ''.join([chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) for char in name])
            return [name, id, hash]
      
      for room in rooms:
            if real_room(room):
                  real_rooms += [decode_room(room)]

with open('output', 'w') as output:
      output.write( str(sum([room[1] for room in real_rooms])) + '\n')
      output.write( str([(name, id) for name, id, hash in real_rooms if 'north' in name][0][1]) + '\n')
