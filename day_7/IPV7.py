import re

with open('input') as input:
    text = input.read()
    ips  = text.split('\n')[:-1]

def ABBA(sequence):
    for i in range(len(sequence) - 3):
        a,b,c,d = sequence[i:i+4]
        if a != b and a == d and b == c:
            return True
    return False

def ABA(sequence):
    results = [ ]
    for i in range(len(sequence) - 2):
        a,b,c = sequence[i:i+3]
        if a != b and a == c:
            results += [ (b, a) ]
    return results

def BAB(sequence, patterns):
    for i in range(len(sequence) - 2):
        a,b,c = sequence[i:i+3]
        if a != b and a == c:
            if (a, b) in patterns:
                return True
    return False

def supernet_hypernet(ip):
    split = re.split(r'\[|\]', ip)
    return split[::2], split[1::2]

def supports_TLS(ip):
    supernet, hypernet = supernet_hypernet(ip)
    return any(list(map(ABBA, supernet))) and not any(list(map(ABBA, hypernet)))

def supports_SSL(ip):
    supernet, hypernet = supernet_hypernet(ip)
    patterns = [ pattern for patterns in map(ABA, supernet) for pattern in patterns ]
    return any([BAB(hypersequence, patterns) for hypersequence in hypernet])

with open('output', 'w') as output:
    output.write( str(sum(map(supports_TLS, ips))) + '\n')
    output.write( str(sum(map(supports_SSL, ips))) + '\n')
