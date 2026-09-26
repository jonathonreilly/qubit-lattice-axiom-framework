#!/usr/bin/env python3
"""Pre-comparison targeted long excursion/winding and zero-slide controls."""
import sys
sys.dont_write_bytecode=True
import argparse
from functools import lru_cache
import itertools as it
import json
from pathlib import Path
import sympy as s
import independent_check as check

def distant_periodic_excursions():
    N=4;coords=list(it.product(range(N),repeat=3));index={x:i for i,x in enumerate(coords)}
    edges=set()
    for x in coords:
        for axis in range(3):
            y=list(x);y[axis]=(y[axis]+1)%N
            edges.add(check.edge(index[x],index[tuple(y)]))
    L={index[x] for x in coords if sum(x)%2==0};R=set(range(len(coords)))-L
    P=frozenset(check.edge(index[x],index[(x[0]+1,x[1],x[2])]) for x in coords if x[0]%2==0)
    m=P-{check.edge(index[(0,0,0)],index[(1,0,0)])}
    examples={'distant_plaquette':[(2,2,2),(3,2,2),(3,3,2),(2,3,2)],
              'winding_axis_cycle':[(0,2,2),(1,2,2),(2,2,2),(3,2,2)]}
    output=[]
    for name,points in examples.items():
        v=[index[x] for x in points]
        old={check.edge(v[0],v[1]),check.edge(v[2],v[3])}
        new={check.edge(v[1],v[2]),check.edge(v[3],v[0])}
        assert old<=m and new<=edges
        target=(m-old)|new
        events,cycles=check.transform(m,target,L,R,edges,check.adjacency(len(coords),edges))
        assert len(cycles)==1 and cycles[0]['approach_slides']>=2
        output.append({'name':name,'torus_side':N,'near_pairs':len(m),'cycle':points,
                       'slides':events,'excursion':cycles[0],'outside_edges_and_both_vacancies_restored':True})
    return output

def zero_slide_cube_deposition():
    coords=list(it.product((0,1),repeat=3))
    edges={check.edge(i,j) for i in range(8) for j in range(i+1,8)
           if sum(abs(a-b) for a,b in zip(coords[i],coords[j]))==1}
    def columnar(m):return len(m)==4 and len({next(i for i in range(3) if coords[a][i]!=coords[b][i]) for a,b in m})==1
    @lru_cache(None)
    def probability(m):
        if len(m)==4:return s.Rational(1),s.Rational(int(columnar(m)))
        targets=[target for kind,data,target in check.own.channels(m,edges) if kind=='birth']
        if not targets:return s.Rational(0),s.Rational(0)
        future=[probability(t) for t in targets]
        return tuple(sum(row[i] for row in future)/len(future) for i in range(2))
    full,columnar_prob=probability(frozenset())
    assert full<1
    return {'kappa':0,'nu':0,'full_packing_probability':str(full),
            'unconditional_columnar_probability':str(columnar_prob),
            'columnar_given_full':str(columnar_prob/full),
            'distinction':'Positive fixed kappa followed by beta/kappa to infinity still eventually fills. Setting kappa=0 first has positive jamming probability.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    result={'long_excursions':distant_periodic_excursions(),'zero_slide_cube':zero_slide_cube_deposition()}
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
