#!/usr/bin/env python3
"""Independent exact rotor-word reconstruction; no publication runner imports."""
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path
A=(0,3,5,6)
B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if (a^b).bit_count()==1)
OMEGA=(tuple(1 if v in A else 0 for v in range(8)), (0,)*12)

def tidy(v): return {s:x for s,x in v.items() if x}
def add(*terms):
    out=defaultdict(Fraction)
    for scalar,v in terms:
        for s,x in v.items(): out[s]+=scalar*x
    return tidy(out)
def action(v, op):
    out=defaultdict(Fraction)
    for state,x in v.items():
        for new,c in op(state): out[new]+=x*c
    return tidy(out)
def hop_op(state,center=None):
    q,E=state
    for k,(a,b) in enumerate(EDGES):
        if center is not None and a!=center: continue
        if q[a] and not q[b]:
            nq=list(q); ne=list(E); s=q[a]
            nq[a]=0; nq[b]=s; ne[k]-=s
            yield (tuple(nq),tuple(ne)),1

def mark_op(k,signs):
    a,b=EDGES[k]
    def op(state):
        q,E=state
        if q[a] or q[b]: return
        for s in signs:
            nq=list(q); ne=list(E)
            nq[a]=s; nq[b]=-s; ne[k]+=s
            yield (tuple(nq),tuple(ne)),1
    return op

def F(v):return action(v,hop_op)
def mark(v,k,signs):return action(v,mark_op(k,signs))
def norm2(v):return sum(x*x for x in v.values())
def grade(s):return sum(s[0][a]==0 for a in A)
def gauss(s):
    q,E=s; d=[0]*8
    for k,(a,b) in enumerate(EDGES):d[a]+=E[k];d[b]-=E[k]
    return all(d[v]==q[v]-(v in A) for v in range(8))
def dump(v):
    return [{'q':s[0],'E':s[1],'numerator':x.numerator,'denominator':x.denominator} for s,x in sorted(v.items())]

omega={OMEGA:Fraction(1)}
F1=F(omega);F2=F(F1);F3=F(F2)
rows=[];checks=0
for k,(a,b) in enumerate(EDGES):
    for label,signs in [('plus',(1,)),('minus',(-1,)),('coherent',(1,-1))]:
        J1=mark(F1,k,signs);J2=mark(F2,k,signs);J3=mark(F3,k,signs)
        R=add((Fraction(1,2),J2),(-1,F(J1)))
        localR=add((-1,action(J1,lambda s:hop_op(s,a))))
        cubic=add((Fraction(1,6),J3),(Fraction(-1,2),F(J2)),(Fraction(1,2),F(F(J1))))
        expected={'plus':(2,4),'minus':(2,2),'coherent':(4,6)}[label]
        assert (norm2(J1),norm2(R))==expected
        assert R==localR
        assert not cubic
        assert all(grade(s)==0 and gauss(s) for s in J1)
        assert all(grade(s)==1 and gauss(s) for s in R)
        assert all(max(abs(e) for e in s[1])<=1 for v in [J1,J2,J3,F(J1),F(J2),F(F(J1))] for s in v)
        checks+=7
        rows.append({'edge':[a,b],'mark':label,'b':str(norm2(J1)),'R_norm2':str(norm2(R)),
                     'cubic_terms_before_cancel':[len(J3),len(F(J2)),len(F(F(J1)))],
                     'cubic_support_after_cancel':len(cubic),
                     'B_words':dump(J1) if k==0 else None,'R_words':dump(R) if k==0 else None})
import sympy as sp
Fmat=sp.zeros(5);jmat=sp.zeros(5)
for n in range(4):Fmat[n+1,n]=1
jmat[0,1]=1
comm=Fmat*jmat-jmat*Fmat
for _ in range(2):comm=Fmat*comm-comm*Fmat
assert comm[:,0]!=sp.zeros(5,1)
checks+=1
result={'primitive_edges':EDGES,'tested_first_marks':len(rows),'checks':checks,'failures':0,
        'load_bearing_identity':'j F^3/6 - F j F^2/2 + F^2 j F/2 = 0 on Omega',
        'scope':'Exact primitive rotor paths, all 36 cube marks; conditional finite-spin extension from unit 0-to-+/-1 transitions.',
        'generic_ladder_counterexample':list(comm[:,0]),'rows':rows}
Path('primitive_word_results.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2,default=str))
print(f'TOTAL: PASS={checks} FAIL=0')
