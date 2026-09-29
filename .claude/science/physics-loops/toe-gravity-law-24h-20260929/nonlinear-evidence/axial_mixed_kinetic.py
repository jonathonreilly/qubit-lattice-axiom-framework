#!/usr/bin/env python3
"""Add the GC degree-two P^2 obligation and optional inherited axial symmetries."""
import ast
from itertools import product
import json
import time
import argparse
from axial_cc import (Q,HERE,assemble,poly,v,bracket,g1,t2,quotient,eliminate,
                      verify_witness,checks,budget)


def density(family, data):
    if family in ('V2','T3'):
        return poly(((1,(v('N'),)+data),))
    if family=='G2':
        return poly(((1,(v('X'),)+data),))
    raise ValueError(family)


def add_gc_kinetic(s):
    for col,name in enumerate(s.names):
        fam,data=name.split(':',1)
        data=ast.literal_eval(data)
        if fam=='T3':
            s.putpoly('GC2_P2',bracket(g1(),density(fam,data)),col)
        elif fam=='G2':
            s.putpoly('GC2_P2',bracket(density(fam,data),t2('N')),col)
        elif fam=='U0':
            xp,np=data
            rhs=poly((c,tuple(a for a in m if a[0]!='N')+(v('X',pos=xp),v('N',pos=np)))
                     for m,c in t2('N').items())
            s.putpoly('GC2_P2',quotient(rhs),col,-1)


def transformed(fam,data,reflection):
    sign=1
    def field(a,edge=False):
        kind,comp,pos=a
        return (kind,comp if reflection else {0:0,1:2,2:1}[comp],
                (1-pos if edge else -pos) if reflection else pos)
    if fam=='V2':out=tuple(sorted(field(a) for a in data))
    elif fam=='T3':out=(field(data[0]),)+tuple(sorted(field(a) for a in data[1:]))
    elif fam=='G2':
        out=tuple(field(a,True) for a in data)
        sign=-1 if reflection else 1
    elif fam=='F1':
        h,ni,mi=data
        if reflection:out=(field(h,True),1-mi,1-ni)
        else:out=(field(h,True),ni,mi)
    elif fam=='U0':
        xp,np=data
        out=(-xp-1,-np) if reflection else data
        sign=-1 if reflection else 1
    elif fam=='V0':
        xp,yp=data
        out=(-yp,-xp) if reflection else data
    else:raise ValueError(fam)
    return fam+':'+repr(out),sign


def add_symmetry(s):
    index={name:i for i,name in enumerate(s.names)}
    for col,name in enumerate(s.names):
        fam,data=name.split(':',1)
        data=ast.literal_eval(data)
        for reflection in (True,False):
            other,sign=transformed(fam,data,reflection)
            target=index[other]
            key=(col,target)
            family='reflection' if reflection else 'yz_exchange'
            s.put(family,key,col,Q(1))
            s.put(family,key,target,Q(-sign))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--symmetry',action='store_true')
    ap.add_argument('--rational',action='store_true')
    ap.add_argument('--radius',type=int,default=1)
    args=ap.parse_args()
    budget();checks()
    start=time.time()
    s=assemble(args.radius,True,True)
    add_gc_kinetic(s)
    if args.symmetry:add_symmetry(s)
    stem=f'axial_r{args.radius}_mixed_kinetic'+('_symmetric' if args.symmetry else '')
    payload=s.save(HERE/(stem+'_system.json'))
    print(json.dumps({'columns':len(s.names),'rows':len(s.rows),'nonzero_entries':sum(map(len,s.rows.values()))}),flush=True)
    result=eliminate(payload,None if args.rational else 1000003)
    result['seconds']=time.time()-start
    (HERE/(stem+('_rational' if args.rational else '_modular')+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    if not result['consistent'] and args.rational:
        print('Exact certificate recombination:',verify_witness(payload,result),flush=True)
    print(json.dumps({k:v for k,v in result.items() if k!='witness'}),flush=True)
    print('Only the frozen axial subsystem is tested; full gravity and axiom implications remain open.',flush=True)


if __name__=='__main__':main()
