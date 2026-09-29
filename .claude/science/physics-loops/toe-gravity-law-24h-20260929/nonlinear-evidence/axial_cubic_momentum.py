#!/usr/bin/env python3
"""Explore G3=P^3 escape; no configuration-only spatial action assumed."""
import argparse
from itertools import combinations_with_replacement
import json
import time
from axial_cc import (Q,HERE,assemble,v,poly,bracket,c1,eliminate,verify_witness,budget)
from axial_mixed_kinetic import add_gc_kinetic


def add_cubic_momentum(s,radius):
    ps=[v('p',i,x) for i in range(3) for x in range(1-radius,radius+1)]
    for mon in combinations_with_replacement(ps,3):
        col=s.new('G3p:'+repr(mon))
        f=poly(((1,(v('X'),)+mon),))
        s.putpoly('GC2_P2',bracket(f,c1('N')),col)
        s.put('continuum_G3p_0',tuple(a[1] for a in mon),col,Q(1))
        for i,a in enumerate(mon):
            key=(a[1],)+tuple(b[1] for j,b in enumerate(mon) if j!=i)
            s.put('continuum_G3p_d',key,col,Q(2*a[2]-1,2))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--radius',type=int,default=1)
    ap.add_argument('--rational',action='store_true')
    a=ap.parse_args();budget();start=time.time()
    s=assemble(a.radius,True,True)
    add_gc_kinetic(s);add_cubic_momentum(s,a.radius)
    stem=f'axial_r{a.radius}_cubic_momentum'
    payload=s.save(HERE/(stem+'_system.json'))
    print(json.dumps({'columns':len(s.names),'rows':len(s.rows),'nnz':sum(map(len,s.rows.values()))}),flush=True)
    result=eliminate(payload,None if a.rational else 1000003)
    result['seconds']=time.time()-start
    (HERE/(stem+('_rational' if a.rational else '_modular')+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    if not result['consistent'] and a.rational:
        print('Exact certificate recombination:',verify_witness(payload,result),flush=True)
    print(json.dumps({k:v for k,v in result.items() if k!='witness'}),flush=True)
    print('Scope: necessary axial subsystem allowing cubic-momentum shift; not full closure.',flush=True)


if __name__=='__main__':main()
