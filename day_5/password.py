import hashlib

with open('input') as input:
      text = input.read()

def md5(word, code):
    return hashlib.md5(bytes(word + code, encoding='utf-8')).hexdigest()

id   = 'reyedfim'

code = 0
results = []
while len(results) < 8:
    hash = md5(id, str(code))
    if hash[0:5] == '00000':
        results += [hash[5]]
    code += 1

simple_password = ''.join(results)

code = 0
results = { }
while len(results) < 8:
    hash = md5(id, str(code))
    if hash[0:5] == '00000':
        if hash[5] in [str(i) for i in range(8)] and not hash[5] in results:
            results[hash[5]] = hash[6]
    code += 1

complex_password = ''.join([ results[str(i)] for i in range(8)])

with open('output', 'w') as output:
      output.write( simple_password  + '\n')
      output.write( complex_password + '\n')
