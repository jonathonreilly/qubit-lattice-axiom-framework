#!/usr/bin/env python3
"""Recover exact affine rational solution from the saved coefficient system."""
from collections import defaultdict
from fractions import Fraction as Q
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')


def solve(payload):
    pivots={}
    for i,row in enumerate(payload['rows']):
        if i%100==0:
            if time.time()>=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch'] or (RUNTIME/'STOP_REQUESTED.json').exists():
                raise RuntimeError('Campaign stop')
        r={j:Q(c) for j,c in row['coefficients']}
        r[-1]=-Q(row['rhs'])
        if not r[-1]: del r[-1]
        while any(j>=0 for j in r):
            p=min(j for j in r if j>=0)
            f=r[p]
            if p not in pivots:
                pivots[p]={j:c/f for j,c in r.items()}
                break
            for j,c in pivots[p].items():
                x=r.get(j,Q(0))-f*c
                if x:r[j]=x
                elif j in r:del r[j]
        else:
            assert not r,('inconsistent',i,r)
    free=sorted(set(range(len(payload['columns'])))-set(pivots))
    solution={j:{j:Q(1)} for j in free}
    for j,row in sorted(pivots.items(),reverse=True):
        expr=defaultdict(Q)
        if -1 in row:expr[-1]=-row[-1]
        for k,c in row.items():
            if k in (-1,j):continue
            for var,x in solution[k].items():expr[var]-=c*x
        solution[j]={k:c for k,c in expr.items() if c}
    # Recombine every row including free coefficients, independently of pivot update.
    for row in payload['rows']:
        residual=defaultdict(Q)
        residual[-1]=-Q(row['rhs'])
        for j,c in row['coefficients']:
            for var,x in solution[j].items():residual[var]+=Q(c)*x
        assert not any(residual.values()),row['id']
    return free,solution


if __name__=='__main__':
    stem=sys.argv[1] if len(sys.argv)>1 else 'axial_r1_mixed'
    payload=json.loads((HERE/(stem+'_system.json')).read_text())
    free,solution=solve(payload)
    output={'free_columns':free,'particular_solution':[str(solution[j].get(-1,0)) for j in range(len(payload['columns']))],
            'affine_solution':[[j,[[k,str(c)] for k,c in sorted(e.items())]] for j,e in sorted(solution.items())]}
    (HERE/(stem+'_solution.json')).write_text(json.dumps(output,separators=(',',':'))+'\n')
    print('Exact affine solution recombined against every assembled equation; free variables',len(free))
    for family in ['V2','G2','F1','U0','V0']:
        print(family)
        for j,name in enumerate(payload['columns']):
            if name.startswith(family+':'):
                expr=solution[j]
                if expr: print(name,{('constant' if k==-1 else 'free_'+str(k)):str(c) for k,c in expr.items()})
