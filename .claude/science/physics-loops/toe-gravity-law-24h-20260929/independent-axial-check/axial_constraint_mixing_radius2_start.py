#!/usr/bin/env python3
"""Broaden necessary subsystem to constraint-ideal mixing vanishing in IR."""
from itertools import product
import argparse
import json
import time
from axial_cc import (Q,HERE,assemble,v,poly,quotient,c1,g1,eliminate,verify_witness,budget)
from axial_mixed_kinetic import add_gc_kinetic
from axial_cubic_momentum import add_cubic_momentum


def add_mixing(s,radius):
    # CC = G[F]+C[Z1(P;N,M)]. C1[Z1] first appears at hP degree2.
    verts=list(range(-radius,radius+1))
    for comp,pp,np,mp in product(range(3),verts,verts,verts):
        if np>=mp:continue
        col=s.new('Z1:'+repr((comp,pp,np,mp)))
        terms=[]
        for mon,c in c1('N').items():
            rest=tuple(a for a in mon if a[0]!='N')+(v('p',comp,pp),)
            terms.extend(((c,rest+(v('N',pos=np),v('M',pos=mp))),
                          (-c,rest+(v('M',pos=np),v('N',pos=mp)))))
        s.putpoly('CC2',quotient(poly(terms)),col,-1)
        s.put('continuum_Z1',(comp,),col,Q(mp-np))
    # GC = C[U]+G[W1(P;X,N)]. W is a bond-centred local kernel.
    edgeverts=list(range(1-radius,radius+1))
    for comp,pp,xp,np in product(range(3),edgeverts,range(-radius,radius+1),edgeverts):
        col=s.new('W1:'+repr((comp,pp,xp,np)))
        terms=[]
        for mon,c in g1().items():
            rest=tuple(a for a in mon if a[0]!='X')
            terms.append((c,rest+(v('p',comp,pp),v('X',pos=xp),v('N',pos=np))))
        s.putpoly('GC2_P2',quotient(poly(terms)),col,-1)
        for tag,moment in [('0',Q(1)),('dp',Q(2*pp-1,2)),('dX',Q(xp)),('dN',Q(2*np-1,2))]:
            s.put('continuum_W1_'+tag,(comp,),col,moment)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--radius',type=int,default=1)
    ap.add_argument('--rational',action='store_true')
    ap.add_argument('--relax-kernel-moments',action='store_true');a=ap.parse_args()
    budget();start=time.time()
    s=assemble(a.radius,True,True);add_gc_kinetic(s);add_cubic_momentum(s,a.radius);add_mixing(s,a.radius)
    if a.relax_kernel_moments:
        # Preserve continuum order of the complete bracket RHS, not a stronger
        # zero first moment for each kernel in isolation. Antisymmetric Z has
        # order>=1 and C1 order2; W order>=1 and G1 order1. These terms are
        # subleading to the prescribed CC order2 and GC order1 respectively.
        omitted={'continuum_Z1','continuum_W1_dp','continuum_W1_dX','continuum_W1_dN'}
        for key in list(s.rows):
            if key[0] in omitted:
                del s.rows[key]
                s.rhs.pop(key,None)
    stem=f'axial_r{a.radius}_constraint_mixing'+('_relaxed' if a.relax_kernel_moments else '')
    payload=s.save(HERE/(stem+'_system.json'))
    print(json.dumps({'columns':len(s.names),'rows':len(s.rows),'nnz':sum(map(len,s.rows.values()))}),flush=True)
    result=eliminate(payload,None if a.rational else 1000003);result['seconds']=time.time()-start
    (HERE/(stem+('_rational' if a.rational else '_modular')+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    if not result['consistent'] and a.rational:print('Exact certificate recombination:',verify_witness(payload,result),flush=True)
    print(json.dumps({k:v for k,v in result.items() if k!='witness'}),flush=True)
    print('Scope: necessary axial subsystem with declared constraint mixing; remaining jet equations open.',flush=True)


if __name__=='__main__':main()
