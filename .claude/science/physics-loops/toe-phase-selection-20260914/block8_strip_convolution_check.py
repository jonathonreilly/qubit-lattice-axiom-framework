#!/usr/bin/env python3
"""Second exact derivation using a factored curl generating polynomial."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

# Three-square strip curl generating function:
# g(z1)^3 g(z2)^2 g(z3)^3 g(z2/z1) g(z3/z2), g(z)=10+9(z+z^-1).
# This uses ten short convolutions, not an enumeration of all link lifts.
columns=[(1,0,0)]*3+[(0,1,0)]*2+[(0,0,1)]*3+[(-1,1,0),(0,-1,1)]
poly={(0,0,0):1}
for column in columns:
    next_poly=defaultdict(int)
    for exponent,coefficient in poly.items():
        next_poly[exponent]+=10*coefficient
        for sign in [-1,1]:
            dest=tuple(x+sign*y for x,y in zip(exponent,column))
            next_poly[dest]+=9*coefficient
    poly=dict(next_poly)
assert sum(poly.values())==28**10
states=list(product([-1,0,1],repeat=3))
anti=[[0,1,-1],[-1,0,1],[1,-1,0]]
def witness(b):
    return [1,-2,1][b[1]+1]*anti[b[0]+1][b[2]+1]
result=Fraction(0)
for b in states:
    for curl,coefficient in poly.items():
        bp=tuple((x+y+1)%3-1 for x,y in zip(b,curl))
        mismatch=tuple((y-x-s)//3 for x,y,s in zip(b,bp,curl))
        result+=Fraction(coefficient*witness(b)*witness(bp),28**10*2**sum(m*m for m in mismatch))
expected=Fraction(-901886967,55267035185152)
assert result==expected and result<0
record=dict(method='Integer Laurent-polynomial convolution with ten factors and factorized 27-state witness',coefficient_count=len(poly),coefficient_sum=sum(poly.values()),exact_quadratic_form=str(result),witness_norm_squared=sum(witness(b)**2 for b in states),factorization='w(b1,b2,b3)=[1,-2,1](b2)*A(b1,b3), A=[[0,1,-1],[-1,0,1],[1,-1,0]]')
Path(__file__).resolve().with_name('BLOCK8_STRIP_CONVOLUTION_CHECK.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
