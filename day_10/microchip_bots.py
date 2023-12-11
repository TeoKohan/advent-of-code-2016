import re

class Output:
    def __init__(self) -> None:
        self.value = None
    
    def give(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f'Output'

class Bot():
    def __init__(self, id) -> None:
        self.id    = id
        self.low   = None
        self.high  = None
        self.value = None
    
    def give(self, value):
        if self.value == None:
            self.value = value
            return None
        else:
            a, b = min(value, self.value), max(value, self.value)
            self.value = None
            A = self.low.give(a)
            B = self.high.give(b)
            A = A if A != None else []
            B = B if B != None else []
            return [(self.id, a, b)] + A + B
    
    def __repr__(self) -> str:
        return f'[bot {self.low} {self.value} {self.high}]'

with open('input') as input:
    text = input.read()

lines = text.split('\n')[:-1]
line  = ''.join(lines)

d = re.compile(r'^(?:value|bot)|(?:bot|output)|\d+')

lines  = [d.findall(line) for line in lines]
values = list(filter(lambda x: x[0] == 'value', lines))
rules  = list(filter(lambda x: x[0] == 'bot', lines))

outputs = dict()
bots    = {n : Bot(n) for (_, n, _, _, _, _) in rules}

def get_output(n):
    if not n in outputs:
        outputs[n] = Output()
    return outputs[n]

for rule in rules:
    _, n, _, _, _, _ = rule
    _, _, s, v, _, _ = rule
    _, _, _, _, t, w = rule

    if s == 'bot':
        bots[n].low  = bots[v]
    else:
        bots[n].low  = get_output(v)
    if t == 'bot':
        bots[n].high = bots[w]
    else:
        bots[n].high = get_output(w)

for value in values:
    _, n, _, b = value
    swaps = bots[b].give(int(n))
    if swaps:
        for swap in swaps:
            i, a, b = swap
            if a == 17 and b == 61:
                chosen_id = i

with open('output', 'w') as output:
    output.write(chosen_id+'\n')
    output.write(str(outputs['0'].value * outputs['1'].value * outputs['2'].value)+'\n')