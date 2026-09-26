#!/usr/bin/env python3
"""Exact tiny extended-chain and closed-trace controls for worm sampling."""
from pathlib import Path
from itertools import product
import sympy as s
import hashlib,json

HERE=Path(__file__).resolve().parent;N=3;checks=[]
def check(name,ok,detail=None):
 assert bool(ok),(name,detail)
 checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
states=[]
for field in product((-1,0,1),repeat=N):
 div=tuple(field[(x+1)%N]-field[(x-1)%N] for x in range(N))
 for head in range(N):
  if div==tuple(int(x==0)-int(x==head) for x in range(N)):states.append((head,field))
index={v:i for i,v in enumerate(states)}
closed=[i for i,v in enumerate(states) if v[0]==0];opened=[i for i in range(len(states)) if i not in closed]
assert len(closed)==3
for z in (s.Rational(1,5),s.Rational(1),s.Rational(4)):
 P=s.zeros(len(states))
 for row,(head,field) in enumerate(states):
  for direction in (-1,1):
   slot=(head+direction)%N;old=field[slot];new=old+direction
   if new not in (-1,0,1):P[row,row]+=s.Rational(1,2);continue
   changed=list(field);changed[slot]=new;nexthead=(head+2*direction)%N
   col=index[nexthead,tuple(changed)];delta=int(new!=0)-int(old!=0)
   acceptance=min(s.S.One,z**delta)
   P[row,col]+=acceptance/2;P[row,row]+=(1-acceptance)/2
 weight=s.Matrix([z**sum(x!=0 for x in field) for head,field in states]);weight/=sum(weight)
 assert weight.T*P==weight.T
 assert s.diag(*weight)*P==P.T*s.diag(*weight)
 trace=P.extract(closed,closed)+P.extract(closed,opened)*(s.eye(len(opened))-P.extract(opened,opened)).inv()*P.extract(opened,closed)
 pi=weight.extract(closed,[0]);pi/=sum(pi)
 assert pi.T*trace==pi.T and trace*s.ones(len(closed),1)==s.ones(len(closed),1)
 expected=s.Matrix([z**N if any(states[i][1]) else 1 for i in closed]);expected/=sum(expected)
 assert pi==expected
 check('extended_and_closed_trace_z_'+str(z),True,dict(extended_states=len(states),closed_states=len(closed),closed_probabilities=[str(v) for v in pi]))
(HERE/'GAUSS_WORM_TRACE_RESULTS.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,scope='Exact 1D three-site implementation control. The general detailed-balance argument is separate; no 3D mixing claim.'),indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
