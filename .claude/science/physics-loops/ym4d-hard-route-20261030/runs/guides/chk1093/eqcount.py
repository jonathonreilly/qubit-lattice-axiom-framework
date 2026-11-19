import re, sys
src = open(sys.argv[1], encoding='utf-8').read().split('\n')
n = 0
for i, line in enumerate(src, 1):
    # count numbered display environments opened on this line
    for m in re.finditer(r'\\begin\{(equation|align|gather|multline)\}', line):
        n += 1
    for lab in re.findall(r'\\label\{(eq:[^}]*)\}', line):
        if lab in ('eq:pre:10-3', 'eq:pre:11-1', 'eq:pre:theorem-mixing', 'eq:pre:10-4', 'eq:pre:11-5'):
            print(lab, 'line', i, 'eq number in section', n)
