"""Exact Pauli contraction with actual cycle domain-wall energies.
Delta=nu=1; fractions retain denominators, no numerical simulation.
Data order i0,j0,i1,j1,Q,P. Independent blocks are 4-bit ancilla masks.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import defaultdict, Counter
ops=[]
for entrance in range(2):
    for H in 'XY':
        for A in 'XYZ':
            for site,char in ((2*entrance,H),(2*entrance+1,H),(4,A),(5,A)):
                ops.append((site,char))
# Pauli phases represented by powers of i, all exact integers.
pair={'XY':(1,'Z'),'YX':(3,'Z'),'YZ':(1,'X'),'ZY':(3,'X'),
      'ZX':(1,'Y'),'XZ':(3,'Y')}
def left_multiply(index, phase, word):
    site,char=ops[index]; old=word[site]; out=list(word)
    if old=='I': out[site]=char
    elif old==char: out[site]='I'
    else:
        exponent,result=pair[char+old]; phase=(phase+exponent)%4; out[site]=result
    return phase,''.join(out)
def energy(mask):
    total=0
    for gadget in range(12):
        bits=(mask>>(4*gadget))&15
        total+=sum(((bits>>r)&1)!=((bits>>((r+1)%4))&1) for r in range(4))
    return total
paths=[]
# All possible four-step final parity patterns in the cat-plus product:
# one bit four times; two bits twice each; four bits of one square.
paths.extend((a,a,a,a) for a in range(48))
for a,b in combinations(range(48),2):
    paths.extend(set(permutations((a,a,b,b))))
for gadget in range(12):
    paths.extend(permutations(range(4*gadget,4*gadget+4)))
raw=defaultdict(F); allowed=Counter()
for path in paths:
    mask=0; phase=0; word='IIIIII'; denom=1
    for step,index in enumerate(path):
        mask^=1<<index
        phase,word=left_multiply(index,phase,word)
        E=energy(mask)
        if step<3:
            if E==0: break  # R excludes all intermediate low returns.
            denom*=E
    else:
        assert E==0
        assert phase in (0,2)
        raw[word]+=F(1 if phase==0 else -1,denom)
        allowed[len(set(index//4 for index in path))]+=1
# Two-step coefficients are direct contractions with energy2.
A=F(48,2); D=F(48,4)
effective={word:-value for word,value in raw.items()}
effective['IIIIII']+=A*D
anti=sum(a//4!=b//4 and ops[a][0]==ops[b][0] and ops[a][1]!=ops[b][1]
         for a,b in combinations(range(48),2))
print('Terms:',len(ops),'cross-gadget anticommuting pairs:',anti)
print('Allowed path counts by number of gadgets:',dict(allowed))
print('Second coefficient =',-A,'; second inverse moment =',D)
print('Raw fourth scalar =',raw['IIIIII'],'; normalization correction =',A*D)
print('Normalized fourth operator:')
for word,coefficient in sorted(effective.items()): print(word,coefficient)
assert anti==132
assert effective['IIIIII']==27
assert len(effective)==13
assert all(v==-F(5,2) for w,v in effective.items() if w!='IIIIII')
print('Exact joint coefficient identities verified.')
