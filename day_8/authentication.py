from abc import ABC, abstractmethod
import re

class Instruction(ABC):
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    @abstractmethod
    def evaluate(self, grid):
        pass

class Light(Instruction):
    def evaluate(self, grid):
        for i in range(self.i):
            for j in range(self.j):
                grid[j][i] = '#'
        return grid

class ShiftRow(Instruction):
    def evaluate(self, grid):
        grid[self.i] = grid[self.i][-self.j:] + grid[self.i][:-self.j]
        return grid

class ShiftCol(Instruction):
    def evaluate(self, grid):
        def shift_column():
            final = grid[-1][self.i]
            for i in reversed(range(1, len(grid))):
                grid[i][self.i] = grid[i-1][self.i]
            grid[0][self.i] = final
        for _ in range(self.j):
            shift_column()
        return grid

with open('input') as input:
    text = input.read()

lines = text.split('\n')[:-1]

d = re.compile(r'rect|row|column|\d+')

def str2ins(s: [str]):
    D = {
        'rect' : Light,
        'row' : ShiftRow,
        'column' : ShiftCol
    }

    return D[s[0]](*map(int, s[1:]))

lines = [d.findall(line) for line in lines]
lines = [str2ins(line) for line in lines]

screen = [['.' for _ in range(50)] for _ in range(6)]

for instruction in lines:
    screen = instruction.evaluate(screen)

def count_lit(screen):
    result = 0
    for i in range(len(screen)):
        for j in range(len(screen[i])):
            result += 1 if screen[i][j] == '#' else 0
    return result

with open('output', 'w') as output:
    output.write(str(count_lit(screen)) + '\n\n')
    for line in screen:
        output.write(''.join(line) + '\n')