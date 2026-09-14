#!/usr/bin/env python3
"""Bounded falsifier of a conjectured generic central-fiber energy ordering.

This is not a cubic-lattice theorem check. The jump systems below are supplied
small integer rows. Any failure limits the generic proof route only.
"""
from itertools import product, combinations_with_replacement
from pathlib import Path
import json, time
import numpy as np
from scipy.linalg import eigh


def test_row(d, rng, trials=4):
    d=np.asarray(d,dtype=int)
    states=np.asarray(list(product((-1,0,1),repeat=len(d))),dtype=int)
    charges=states@d
    f=states[(charges==0)&np.any(states!=0,axis=1)]
    f=np.asarray([v for v in f if v[np.flatnonzero(v)[0]]==1])
    if not len(f): return []
    index={tuple(v):i for i,v in enumerate(states)}
    rows=[]
    for trial in range(trials):
        weights=np.ones(len(f)) if trial==0 else np.exp(rng.uniform(-2,2,len(f)))
        g=0 if trial%2==0 else 0.2
        matrix=np.diag(g*np.sum(states*states,axis=1)).astype(float)
        for jump,w in zip(f,weights):
            for i,v in enumerate(states):
                for s in (-1,1):
                    j=index.get(tuple(v+s*jump))
                    if j is not None: matrix[j,i]-=w
        neutral=np.flatnonzero(charges==0)
        en=float(eigh(matrix[np.ix_(neutral,neutral)],subset_by_index=(0,0),eigvals_only=True)[0])
        best=(en,0)
        for q in np.unique(charges):
            if q<=0: continue
            ids=np.flatnonzero(charges==q)
            eq=float(eigh(matrix[np.ix_(ids,ids)],subset_by_index=(0,0),eigvals_only=True)[0])
            if eq<best[0]-1e-10: best=(eq,int(q))
        row={'d':d.tolist(),'jump_count':len(f),'trial':trial,'g':g,'neutral_energy':en,
             'best_charge':best[1],'best_energy':best[0],'difference':best[0]-en}
        if best[1]:
            row['jumps']=f.tolist();row['weights']=weights.tolist()
        rows.append(row)
        if best[1]: break
    return rows


def main():
    start=time.monotonic();rng=np.random.default_rng(9142026);results=[]
    for n in (4,5,6):
        for d in combinations_with_replacement(range(1,5),n):
            results+=test_row(d,rng)
            failures=[x for x in results if x['best_charge']]
            if failures or time.monotonic()-start>90:
                break
        if failures or time.monotonic()-start>90: break
    out={'status':'exploratory_non_geometric_falsifier','elapsed_seconds':time.monotonic()-start,
         'case_count':len(results),'failures':failures,'results':results}
    Path(__file__).with_name('BLOCK2_DISCRETE_SECTOR_PROBE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))

if __name__=='__main__':main()
