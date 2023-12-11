import re

with open('input') as input:
    text = input.read()

lines = text.split('\n')[:-1]
line = ''.join(lines)

d = re.compile(r'\((\d+)x(\d+)\)')

def V1(line):
    result = 0
    while(line != ''):
        if m := d.match(line):
            match_length = sum(map(len, m.groups())) + 3

            length, times = map(int, m.groups())
            line   = line[match_length:]
            repeat = line[:length]
            line   = line[length:]
            result += times * len(repeat)
        else:
            result += 1
            line = line[1:]
    return result

def V2(line):
    result = 0
    while(line != ''):
        if m := d.match(line):
            match_length = sum(map(len, m.groups())) + 3

            length, times = map(int, m.groups())
            line   = line[match_length:]
            repeat = line[:length]
            line   = line[length:]
            result += times * V2(repeat)
        else:
            result += 1
            line = line[1:]
    return result

with open('output', 'w') as output:
    output.write(str(V1(line))+'\n')
    output.write(str(V2(line))+'\n')